# -*- coding: utf-8 -*-
import scrapy
import json
from  getComment.items import GetcommentItem
import codecs
#需要假如cookie，不然有些页面没有权限
class GetcommentSpider(scrapy.Spider):
    name = "getComment"
    allowed_domains = ["douban.com"]
    start_urls = ['https://movie.douban.com/subject/26652816/comments?start=35&limit=20&sort=new_score']
    '''
    def __init__(self):
        file=open('film_URL.json')
        for line in file.readlines():
            js=json.loads(line)
            url=js['url']+'comments'
            self.start_urls.append(url)
        file.close()
    '''
    
    def parse(self, response):
        filmname=response.xpath('//*[@id="content"]/h1/text()').extract()[0]
        #extract()返回的是一个列表，里面第一个元素是unicode字符串
        file=codecs.open(filmname,'ab',encoding='utf-8')
        next=response.xpath('//*[@id="paginator"]/a[@class="next"]/@href').extract()
        item=GetcommentItem()
        item['comment']=response.xpath('//*[@id="comments"]/div[@class="comment-item"]/div[2]/p/text()').extract()
        item['title']  =response.xpath('//*[@id="comments"]/div[@class="comment-item"]/div[2]/h3/span[2]/span[1]/@title').extract()
        commentlines = json.dumps(dict(item),ensure_ascii=False) + "\n"
        file.write(commentlines)
        if next:
            next_url=response.url.split('?')[0]+next[0]
            return scrapy.Request(next_url,self.parse)
