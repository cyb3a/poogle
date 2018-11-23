# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from polrepcrawl.items import PoliceReport


class GetreportdataSpider(scrapy.Spider):
    """
    Get 'relevant' data from a policereport

    Run spider with:
    > scrapy crawl getreportdata
    """
    name = 'getreportdata'

    BASE_URL = 'https://www.berlin.de'

    allowed_domains = ['berlin.de']

    def start_requests(self):
        with open('loc-policereport-paths.txt', 'r') as fd:
            for policeReportPath in fd.read().splitlines():
                yield scrapy.Request("https://www.berlin.de{path}".format(path=policeReportPath), meta={'IsLocationInHeader': 'true'})

        with open('noloc-policereport-paths.txt', 'r') as fd:
            for policeReportPath in fd.read().splitlines():
                yield scrapy.Request("https://www.berlin.de{path}".format(path=policeReportPath), meta={'IsLocationInHeader': 'false'})

    def parse(self, response):

        if response.status != 200:
            with open('urls-not-ok.txt', 'a') as fd:
                fd.write("%s\n" % url)
        else:

            """
            Filter police report from whole web page
            """
            relevant= response.xpath(
                '//div[contains(@class,"html5-section") and contains(@class, "article")]')

            """
            Title of police report
            """
            title=relevant.xpath(
                'descendant::h1[contains(@class,"title")]/text()').extract_first()

            """
            Contains date and location
            """
            policeReportHeader=relevant.xpath(
                'descendant::div[contains(@class,"polizeimeldung")]/text()').extract()

            header=" ".join(policeReportHeader)

            """
            Content of police report as one string
            - Excluded police report nr
            """
            rawContent=relevant.xpath(
                'descendant::div[contains(@class,"textile")]/descendant::*/text()').extract()
            content=" ".join([parag.strip(' \t\n\r')
                             for parag in rawContent]).strip(' ')

            """
            Day when data was fetched
            """
            createdAt=datetime.datetime.today().strftime('%Y-%m-%d')



            currentPoliceReport=PoliceReport()
            currentPoliceReport['Title']=title
            currentPoliceReport['Header']=header
            currentPoliceReport['Content']=content
            currentPoliceReport['URL']=response.url
            currentPoliceReport['CreatedAt']=createdAt
            currentPoliceReport['IsLocationInHeader']=response.meta['IsLocationInHeader']
            yield currentPoliceReport
