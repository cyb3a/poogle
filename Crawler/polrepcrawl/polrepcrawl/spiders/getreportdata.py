# -*- coding: utf-8 -*-
import scrapy
import datetime
import re
from polrepcrawl.items import PoliceReport


class GetreportdataSpider(scrapy.Spider):
    """
    Get 'relevant' data from a policereport

    Run spider with:
    > scrapy crawl getreportdata -a filename=policereport-paths.txt
    """
    name = 'getreportdata'

    BASE_URL = 'https://www.berlin.de'

    """
    Berlin districts as set. Retrieved from: https://www.berlin.de/special/immobilien-und-wohnen/stadtteile/uebersicht-nach-bezirken/ 
    """
    BERLIN_DISTRICTS = {'Mitte', 'Friedrichshain-Kreuzberg', 'Pankow', 'Charlottenburg-Wilmersdorf', 'Spandau', 'Steglitz-Zehlendorf',
                        'Tempelhof-Schöneberg', 'Neukölln', 'Treptow-Köpenick', 'Marzahn-Hellersdorf', 'Lichtenberg', 'Reinickendorf'}

    allowed_domains = ['berlin.de']

    def __init__(self, filename=None):
        if filename:
            with open(filename, 'r') as fd:
                policeReportUrls = ["https://www.berlin.de{path}".format(
                    path=policeReportPath) for policeReportPath in fd.read().splitlines()]
                self.start_urls = policeReportUrls

    def parse(self, response):

        urlIdRegex = re.search('pressemitteilung.(\d+).php$', response.url)
        if urlIdRegex is not None:
            url = urlIdRegex.group(1)
        else:
            print("Couldn't get url id for url=%s" % (response.url))
            url = response.url
            with open('urls-no-id.txt', 'a') as fd:
                fd.write("%s\n" % url)

        if response.status != 200:
            with open('urls-not-ok.txt', 'a') as fd:
                fd.write("%s\n" % url)
        else:

            """
            Filter police report from whole web page
            """
            relevant = response.xpath(
                '//div[contains(@class,"html5-section") and contains(@class, "article")]')

            """
            Title of police report
            """
            title = relevant.xpath(
                'descendant::h1[contains(@class,"title")]/text()').extract_first()

            """
            Some police reports are grouped and displayed in one website
            """
            listOfIds = relevant.xpath(
                'descendant::strong/text()').re('^Nr. (\d+)')

            """
            Contains date and location
            """
            policeReportHeader = relevant.xpath(
                'descendant::div[contains(@class,"polizeimeldung")]/text()').extract()

            dates = sum([re.findall('(\d{2}.\d{2}.\d{4})', line) for line in policeReportHeader if re.match(
                '.*(\d{2}\.\d{2}\.\d{4}).*', line)], [])

            locationPreparation = set(sum([line.split("/") for line in policeReportHeader],[]))
            locations = list(locationPreparation & GetreportdataSpider.BERLIN_DISTRICTS)

            """
            Content of police report as one string
            - Excluded police report nr
            """
            rawContent = relevant.xpath(
                'descendant::div[contains(@class,"textile")]/descendant::*/text()').extract()
            content = " ".join([parag.strip(' \t\n\r') for parag in rawContent if (
                not(re.match('^Nr. \d+', parag)))]).strip(' ')

            """
            Day when data was fetched
            """
            createdAt = datetime.datetime.today().strftime('%Y-%m-%d')

            for policeReportId in listOfIds:
                currentPoliceReport = PoliceReport()
                currentPoliceReport['Id'] = policeReportId
                currentPoliceReport['Title'] = title
                currentPoliceReport['Dates'] = dates
                currentPoliceReport['Locations'] = locations
                currentPoliceReport['Content'] = content
                currentPoliceReport['URL'] = url
                currentPoliceReport['CreatedAt'] = createdAt
                yield currentPoliceReport
