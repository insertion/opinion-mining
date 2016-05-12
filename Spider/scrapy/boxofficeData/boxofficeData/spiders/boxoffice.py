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
        tr=response.xpath('//tr[@class="colora"]')
        for td in tr:
            item=BoxofficedataItem()
            item['film_name']=td.xpath('td[1]/a/@title').extract()[0].encode('utf-8')
            item['film_year']=td.xpath('td[7]/text()').extract()
            item['boxoffice']=td.xpath('td[3]/text()').extract()
            item['film_month']='王雷'
            #items.append(item)
            yield item
        #file = open('page.html','wb')
        #file.write(items)
        #file.close()
        pass
