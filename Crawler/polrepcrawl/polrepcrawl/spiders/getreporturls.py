# -*- coding: utf-8 -*-
import scrapy


class GetreporturlsSpider(scrapy.Spider):
    """
    Get all police report url ids from https://www.berlin.de/polizei/polizeimeldungen/archiv/*
    * is a wildcard for a year like 2018

    Run spider with:
    > scrapy crawl getreporturls
    """
    name = 'getreporturls'

    BASE_URL = 'https://www.berlin.de'

    allowed_domains = ['berlin.de']
    start_urls = [
        BASE_URL+'/polizei/polizeimeldungen/archiv/2014/',
        BASE_URL+'/polizei/polizeimeldungen/archiv/2015/',
        BASE_URL+'/polizei/polizeimeldungen/archiv/2016/',
        BASE_URL+'/polizei/polizeimeldungen/archiv/2017/',
        BASE_URL+'/polizei/polizeimeldungen/archiv/2018/'
        ]

    def parse(self, response):
        """
        Get police report paths for each page and write/append to textfile

        Example: 
        > path = '/polizei/polizeimeldungen/pressemitteilung.777777.php'
        """

        """
        We split the paths in two categories
        * onePoliceReportPaths: Each path covers only one police report
        * multiplePoliceReportPaths: Each path covers multiple police reports 

        And safe them in different files
        """

        relevant = response.xpath("//div[contains(@class,'html5-section') and contains(@class,'body')]/ul/li")

        onePoliceReportPaths = relevant.xpath("div[span/strong[contains(text(),'Ereignisort')]]/a/@href").extract()
        multiplePoliceReportPaths =  relevant.xpath("div[not(span)]/a/@href").extract()


        with open('one-policereport-paths.txt', 'a') as fd:
            for path in onePoliceReportPaths:
                fd.write("%s\n" % path)
        with open('multiple-policereport-paths.txt', 'a') as fd:
            for path in multiplePoliceReportPaths:
                fd.write("%s\n" % path)
        """
        Get next page
        """
        pagination = response.xpath('//div[contains(@class,"pagination")]')
        nextPage = pagination.xpath(
            'ul/li[contains(@class,"pager-item-next") and not(contains(@class,"disabled"))]/a/@href').extract_first()
        if nextPage is not None:
            yield response.follow((GetreporturlsSpider.BASE_URL+nextPage), callback=self.parse)
