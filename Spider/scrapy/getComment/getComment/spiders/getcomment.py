# -*- coding: utf-8 -*-
import scrapy
import json
from  getComment.items import GetcommentItem

class GetcommentSpider(scrapy.Spider):
    name = "getcomment"
    allowed_domains = ["douban.com"]
    start_urls = []
    def __init__(self):
        file=open('film_URL.json')
        for line in file.readlines():
            js=json.loads(line)
            url=js['url']+'comments'
            self.start_urls.append(url)
        file.close()
    
    
    def parse(self, response):
        filmname=response.xpath('//*[@id="content"]/h1/text()').extract()[0]
        #extract()返回的是一个列表，里面第一个元素是unicode字符串
        file=open(fillname,'wa')
        next=response.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract()
        item=GetcommentItem()
        item('comment')=response.xpath('//*[@id="comments"]/div[@class="comment-item"]/div[2]/p/text()').extract()
        item('title')  =response.xpath('//*[@id="comments"]/div[@class="comment-item"]/div[2]/h3/span[2]/span[1]/@title').extract()
        commentlines = json.dumps(dict(item),ensure_ascii=False) + "\n"
        file.write(commentlines)
        if next:
            next_url=request.url.split('?')[0]+next[0]
            return scrapy.request(next_url,parse)