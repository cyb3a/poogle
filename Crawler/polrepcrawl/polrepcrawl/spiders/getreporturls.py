# -*- coding: utf-8 -*-
import scrapy


class GetreporturlsSpider(scrapy.Spider):
    name = 'getreporturls'

    BASE_URL = 'https://www.berlin.de'

    allowed_domains = ['berlin.de']
    start_urls = [
        BASE_URL+'/polizei/polizeimeldungen/archiv/2014/',
	    BASE_URL+'/polizei/polizeimeldungen/archiv/2015/',
	    BASE_URL+'/polizei/polizeimeldungen/archiv/2016/',
	    BASE_URL+'/polizei/polizeimeldungen/archiv/2017/', 
	    BASE_URL+'/polizei/polizeimeldungen/archiv/2018/']

    def parse(self, response):
        pass
