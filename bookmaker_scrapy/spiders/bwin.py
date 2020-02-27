# -*- coding: utf-8 -*-
import scrapy


class BwinSpider(scrapy.Spider):
    name = 'bwin'
    allowed_domains = ['bwin.com']
    start_urls = ['https://sports.bwin.es/es/sports#sportId=4']

    def parse(self, response):
        # We are not able to extract... We have to deal with Javascript
        section = response.xpath('//div[@id="marketgridwidget_international"]')
        rows = section.xpath('.//*/table[@class="mg-table"]/tr')
        for row in rows:
            if (row.xpath('@class')):
                match = row.xpath('./td[contains(@class, "mg-event-name-column")]/div/a/span/text()').extract()
                odds = row.xpath('./td[contains(@class, "mg-result-column")]/div[contains(@class, "mg-result-column3")]/*/tr/td/div/button/div/text()').extract()

                yield {
                    'match': match,
                    'odds': odds,
                }
