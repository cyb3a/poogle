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
        # BASE_URL+'/polizei/polizeimeldungen/archiv/2014/',
        # BASE_URL+'/polizei/polizeimeldungen/archiv/2015/',
        # BASE_URL+'/polizei/polizeimeldungen/archiv/2016/',
        # BASE_URL+'/polizei/polizeimeldungen/archiv/2017/',
        BASE_URL+'/polizei/polizeimeldungen/archiv/2018/'
        ]

    def parse(self, response):
        """
        Get police report url ids for each page and write/append to textfile

        Example: 
        > From path = '/polizei/polizeimeldungen/pressemitteilung.777777.php'
        > Get 777777 as police report url id
        """
        policeReportUrlIds = response.xpath("//ul/li/div/a/@href").re('^\/polizei\/polizeimeldungen\/pressemitteilung.(\d+).php')
        with open('policereport-urlids.txt', 'a') as fd:
            for urlId in policeReportUrlIds:
                fd.write("%s\n" % urlId)
        """
        Get next page
        """
        pagination = response.xpath('//div[contains(@class,"pagination")]')
        nextPage = pagination.xpath(
            'ul/li[contains(@class,"pager-item-next") and not(contains(@class,"disabled"))]/a/@href').extract_first()
        if nextPage is not None:
            yield response.follow((GetreporturlsSpider.BASE_URL+nextPage), callback=self.parse)
