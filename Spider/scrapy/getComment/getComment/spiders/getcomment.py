# -*- coding: utf-8 -*-
import scrapy
import json
from  getComment.items import GetcommentItem
import codecs
#需要加入cookie，不然有些页面没有权限
class GetcommentSpider(scrapy.Spider):
    name = "getComment"
    allowed_domains = ["douban.com"]
    cookie={ '__utma':"30149280.901747088.1445074673.1463148044.1463205092.69",
             '__utma':"223695111.47263706.1446025707.1463148044.1463205092.27",
             '__utmb':"30149280.0.10.1463205092",
             '__utmb':"223695111.0.10.1463205092",
             '__utmc':"30149280",
             '__utmc':"223695111",
             '__utmv':"30149280.13938",
             '__utmz':"30149280.1463051064.63.51.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
             '__utmz':"223695111.1463035423.19.13.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
             '_pk_id.100001.4cf6':"54f6d2f316960e51.1446025708.27.1463205379.1463148922.",
             '_pk_ref.100001.4cf6':'["","",1463204969,"http://www.baidu.com/link?url=YQLEs5QV1zmk47dXRps0dqtoMVwYwRFUN5-N9639eoU21p9BFeaxhNRstgUq9Vvs&wd=&eqid=f68d50f40003ae9a000000035734261a"]',
             '_pk_ses.100001.4cf6':"*",
             'ap':"1",
             'bid':'"8P5Iz4n5Ws8"',
             'ck':"8vtY",
             'ct':"y",
             'dbcl2':'"59034306:TCI0yjpqBT4"',
             'gr_user_id':"8121958b-b647-4f44-bc4a-6ce28baf2d5d",
             'll':'"118163"',
             'ps':"y",
             'push_doumail_num':"38",
             'push_noty_num':"6",
             'ue':'"398758695@qq.com"',
             'viewed':'"1756954_1052241_1831698_25952655_1231361_7906768_24703171_3288908_2305237_6510682"',
    }
    #cookie是个字典
    start_urls = []
    
    def __init__(self):
        file=open('film_URL.json')
        for line in file.readlines():
            js=json.loads(line)
            url=js['url']+'comments'
            self.start_urls.append(url)
        file.close()
    
    def parse(self, response):
        filmname=response.xpath('//*[@id="content"]/h1/text()').extract()[0]+'.json'
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
            return scrapy.Request(next_url,self.parse,cookies=self.cookie)
