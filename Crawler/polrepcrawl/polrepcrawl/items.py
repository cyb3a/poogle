# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoliceReport(scrapy.Item):
    Title = scrapy.Field()
    Header = scrapy.Field()
    Content = scrapy.Field()
    IsLocationInHeader = scrapy.Field()
    URL = scrapy.Field()
    CreatedAt = scrapy.Field()

