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

    def getMinDate(self, d):
        acc = []
        for e in d:
            acc.append(datetime.strptime(e, '%d.%m.%Y'))

        return min(acc)

    def parse(self, response):

        relevant = response.xpath(
            '//div[contains(@class,"html5-section") and contains(@class, "article")]')
        # print('RELEVANT {}'.format(relevant))

        policeReportHeader = relevant.xpath(
            'descendant::div[contains(@class,"polizeimeldung")]/text()').extract()
        # print('HEADER LIST: {}'.format(type(policeReportHeader)))

        dates = sum([re.findall('(\d{2}.\d{2}.\d{4})', line) for line in policeReportHeader if re.match(
            '.*(\d{2}\.\d{2}\.\d{4}).*', line)], [])

        # convert date strings to datetime format
        dateList = []
        for e in dates:
            dateList.append(datetime.strptime(e, '%d.%m.%Y'))

        print('EARLIEST DATE: {}'.format(min(dateList)))