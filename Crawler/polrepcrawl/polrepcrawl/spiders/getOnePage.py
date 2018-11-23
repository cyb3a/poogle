# -*- coding: utf-8 -*-
import scrapy
from datetime import datetime
import re

"""
    Get one page for test sake
"""


class GetOnePageSpider(scrapy.Spider):
    name = 'GetOnePage'

    # entry point to generate request for parse()
    def start_requests(self):
        oneUrl = 'https://www.berlin.de/polizei/polizeimeldungen/pressemitteilung.148221.php'
        return [scrapy.Request(url=oneUrl, callback=self.parse)]

    def parse(self, response):

        relevant = response.xpath(
            '//div[contains(@class,"html5-section") and contains(@class, "article")]')

        policeReportHeader = relevant.xpath(
            'descendant::div[contains(@class,"polizeimeldung")]/text()').extract()

        dates = sum([re.findall('(\d{2}.\d{2}.\d{4})', line) for line in policeReportHeader if re.match(
            '.*(\d{2}\.\d{2}\.\d{4}).*', line)], [])

        # convert date strings to datetime format
        dateList = []
        for date in dates:
            dateList.append(datetime.strptime(date, '%d.%m.%Y'))

        print('EARLIEST DATE: {}'.format(min(dateList)))