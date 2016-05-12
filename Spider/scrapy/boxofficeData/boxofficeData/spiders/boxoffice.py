# -*- coding: utf-8 -*-
import scrapy
from boxofficeData.items import BoxofficedataItem
class BoxofficeSpider(scrapy.Spider):
    name = "boxoffice"
    allowed_domains = ["cbooo.cn"]
    start_urls = [
        'http://www.cbooo.cn/year?year=2008'
    ]
    def parse(self, response):
        items=[]
        #file = open('page.html','wb')
        #file.write(response.body)
        #file.close()
        tr=response.xpath('//tr[@class="colora"]')
        for td in tr:
            item=BoxofficedataItem()
            #file.write(td.xpath('td[1]/a/@title').extract())
            item['film_name']=td.xpath('td[1]/a/@title').extract()
            item['film_year']=td.xpath('td[7]/text()').extract()
            item['boxoffice']=td.xpath('td[3]/text()').extract()
            #item['film_month']='王雷'
            items.append(item)
            #yield item
        #file.close()
        return items
        
