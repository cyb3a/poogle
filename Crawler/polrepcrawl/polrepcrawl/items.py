# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class PoliceReport(scrapy.Item):
    Id = scrapy.Field()
    Title = scrapy.Field()
    Dates = scrapy.Field()
    Locations = scrapy.Field()
    Content = scrapy.Field()
    URL = scrapy.Field()
    CreatedAt = scrapy.Field()

