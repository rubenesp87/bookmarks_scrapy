# -*- coding: utf-8 -*-
import scrapy


class BetfairSpider(scrapy.Spider):
    name = 'betfair'
    allowed_domains = ['betfair.es']
    start_urls = ['https://www.betfair.es/sport/football/la-liga-espa%C3%B1ola/117']

    def parse(self, response):
        sections = response.xpath('//li[contains(@class, "section")]')
        for section in sections:
            dates = section.xpath('./div/span[@class="section-header-label"]/text()')
            matches = section.xpath('.//*/div[contains(@class, "event-information")]')
            for match in matches:
                yield {
                    'date': dates.extract(),
                    'match': match.xpath('.//*/span[@class="team-name"]/text()').extract(),
                    'odds': match.xpath('.//*/div[@class="details-market market-3-runners"]/*/ul[@class="runner-list-selections"]/li/a/span/text()').extract(),
                }
