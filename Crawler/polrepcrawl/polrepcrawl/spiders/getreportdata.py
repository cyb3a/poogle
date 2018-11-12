# -*- coding: utf-8 -*-
import scrapy


class GetreportdataSpider(scrapy.Spider):
    """
    Get 'relevant' data from a policereport

    Run spider with:
    > scrapy crawl getreportdata -a filename=policereport-urlids.txt
    """
    name = 'getreportdata'

    BASE_URL = 'https://www.berlin.de'

    allowed_domains = ['berlin.de']

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as fd:
                policeReportUrls = ["https://www.berlin.de/polizei/polizeimeldungen/pressemitteilung.{id}.php".format(
                    id=urlId) for urlId in fd.read().splitlines()]
                self.start_urls = policeReportUrls
                print(policeReportUrls)


    def parse(self, response):
        """
        TODO Get relevant data from a policereport

        HINT: tag with class="html5-section article" contains all relevant data
        """
