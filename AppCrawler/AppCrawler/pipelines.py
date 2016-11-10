# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class AppcrawlerPipeline(object):
    def process_item(self, item, spider):
        print "*******************************************************"
#        print item['name'] 
#        print item["Price"]
#        print item["Genre"] 
#        print item["Downloads"]
#        print item["Rating"]
#        print item["Review_number"]
#        print item["Updated"] 
#        print item["Author"]
#        print item["Version"] 
        print "*******************************************************"
        return item
