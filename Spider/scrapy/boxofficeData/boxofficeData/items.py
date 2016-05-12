# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BoxofficedataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    film_name=scrapy.Field()
    film_year=scrapy.Field()
    film_month=scrapy.Field()
    boxoffice=scrapy.Field()
    pass
