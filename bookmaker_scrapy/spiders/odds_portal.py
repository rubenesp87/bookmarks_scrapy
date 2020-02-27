# -*- coding: utf-8 -*-
import scrapy


class OddsPortalSpider(scrapy.Spider):
    name = 'odds_portal'
    allowed_domains = ['oddsportal.com']
    start_urls = ['https://www.oddsportal.com/soccer/spain/laliga/']

    def parse(self, response):
        section = response.xpath('//table[@id="tournamentTable"]')
        rows = section.xpath('./tbody/tr/text()')
        for row in rows:
            yield {
                'match': row.extract(),
            }
