#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
#from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.selector import Selector
from AppCrawler.items import AppCrawlerItem 

class AppSpider(scrapy.Spider):
    name = "App"

    allowed_domains = ["play.google.com"]
    #start_urls = ["https://play.google.com/store/apps"]
    #start_urls = ["https://play.google.com/store/apps/details?id=com.supercell.clashroyale"]
    start_urls = ["https://play.google.com/store/apps/details?id=com.john.plasmasky",
            "https://play.google.com/store/apps/details?id=com.supercell.clashroyale"]
    #rules = [Rule(LinkExtractor(allow=(r'apps',),deny=(r'reviewId')),follow=True,callback='parse_link')]

    def parse(self, response):
        sel = Selector(response)
        item = AppCrawlerItem()
#        item["Link"] = '' # n(titles.select('head/link[5]/@href').extract())
        item["name"] = sel.xpath('//*[@class="document-title"]/div/text()').extract()
        item["Price"] = sel.xpath('//*[@class="price buy id-track-click"]/span[2]/text()').extract()
        item["Genre"] = sel.xpath('//*[@itemprop="genre"]/text()').extract()
        item["Downloads"] = sel.xpath('//*[@itemprop="numDownloads"]/text()').extract()
        item["Rating"] = sel.xpath('//*[@class="score"]/text()').extract()
        item["Review_number"] = sel.xpath('//*[@class="reviews-num"]/text()').extract()
        item["Updated"] = sel.xpath('//*[@itemprop="datePublished"]/text()').extract()
        item["Version"] = sel.xpath('//*[@itemprop="softwareVersion"]/text()').extract()
        item["Author"] = sel.xpath('//*[@itemprop="author"]/a/span/text()').extract()

        return item
      

