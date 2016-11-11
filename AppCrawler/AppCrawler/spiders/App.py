#!/usr/bin/env python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from AppCrawler.items import AppCrawlerItem 
from scrapy.spiders import Rule, CrawlSpider

class AppSpider(CrawlSpider):
    name = "App"
    allowed_domains = ["play.google.com"]
    start_urls = [
        'http://play.google.com/',
        'https://play.google.com/store/apps/details?id=air.net.machinarium.Machinarium.GP'
    ]

    rules =( 
        Rule(LinkExtractor(allow=("https://play\.google\.com/store/apps/details", )), callback = 'parse_item', follow = True),
    )

    def parse_item(self, response):
        if response.url.find('reviewId') != -1: 
            return;
        item = AppCrawlerItem()
    
        item["URL"] = response.url
        item["Name"] = response.xpath('//div[@class="id-app-title"]/text()').extract()
        item["Downloads"] = response.xpath("//div[@itemprop='numDownloads']/text()").extract()
        item["Updated"] = response.xpath("//div[@itemprop='datePublished']/text()").extract()
        item["Version"] = response.xpath('//div[@itemprop="softwareVersion"]/text()').extract()
        item["Review_number"] = response.xpath("//span[@class='reviews-num']/text()").extract()
        item["Rating"] = response.xpath("//div[@class='score']/text()").extract()
        item["Author"] = response.xpath('//div[@itemprop="author"]/a/span/text()').extract()
        item["Genre"] = response.xpath('//span[@itemprop="genre"]/text()').extract()

        yield item

