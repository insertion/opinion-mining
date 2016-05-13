# -*- coding: utf-8 -*-
import scrapy
import json
from Filmcomment.items import FilmcommentItem
class GeturlSpider(scrapy.Spider):
    name = "douban"
    start_urls = []
    allowed_domains = ["douban.com"]
    def __init__(self):
       file=open('items.json')
       url_head='https://movie.douban.com/subject_search?search_text='
       for line in file.readlines():
            js=json.loads(line)
            url=url_head+js['film_name'][0]
            self.start_urls.append(url)
       file.close()

    def parse(self, response):
        item=FilmcommentItem()
        item['name']=response.xpath('//table[1]/tr[@class="item"]/td/a/@title').extract()
        item['url']=response.xpath('//table[1]/tr[@class="item"]/td/a/@href').extract()
        return item
# response.xpath('//table[3]/tr[@class="item"]/td/a/@href').extract()