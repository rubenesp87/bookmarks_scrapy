# -*- coding: utf-8 -*-
import scrapy


class Bet365Spider(scrapy.Spider):
    name = 'bet365'
    allowed_domains = ['bet365.es']
    start_urls = ['https://www.bet365.es/#/AC/B1/C1/D13/E42493286/F2/']
    download_delay = 5.0

    def parse(self, response):
        # We are not able to extract... We have to deal with Javascript
        sections = response.xpath('//div[@class="wc-WebConsoleModule"]') 
        print(sections)
        # for section in sections:
        #     dates = section.xpath('.//*/h2/span/text()')
        #     yield {
        #         'dates': dates.extract()
        #     }
