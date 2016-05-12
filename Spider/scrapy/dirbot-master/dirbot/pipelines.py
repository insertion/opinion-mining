from scrapy.exceptions import DropItem

import codecs
import json
class FilterWordsPipeline(object):
    """A pipeline for filtering out items which contain certain words in their
    description"""

    # put all words in lowercase
    def __init__(self):
        self.file = codecs.open('items.json','wb',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + "\n"
        #line=unicode.encode(line,'utf-8');
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()