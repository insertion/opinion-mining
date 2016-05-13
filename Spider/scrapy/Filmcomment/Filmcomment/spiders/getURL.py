# -*- coding: utf-8 -*-
import scrapy


class GeturlSpider(scrapy.Spider):
    name = "getURL"
    allowed_domains = ["douban.com"]
    url='https://movie.douban.com/subject_search?search_text='
    start_urls = [
        'https://movie.douban.com/subject_search?search_text=港囧',
    ]
#request的callback函数默认是parse
    def parse(self, response):
        pass
