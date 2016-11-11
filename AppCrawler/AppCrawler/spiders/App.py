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
        if response.url.find('reviewId') != -1: return;
        item = AppCrawlerItem()
    
        item["URL"] = response.url[0]
        item["Name"] = response.xpath('//div[@class="id-app-title"]/text()').extract_first()
        item["Downloads"] = response.xpath("//div[@itemprop='numDownloads']/text()").extract_first()
        item["Updated"] = response.xpath("//div[@itemprop='datePublished']/text()").extract_first()
        item["Version"] = response.xpath('//div[@itemprop="softwareVersion"]/text()').extract_first()
        item["Review_number"] = response.xpath("//span[@class='reviews-num']/text()").extract_first()
        item["Rating"] = response.xpath("//div[@class='score']/text()").extract_first()
        item["Author"] = response.xpath('//div[@itemprop="author"]/a/span/text()').extract_first()
        item["Genre"] = response.xpath('//span[@itemprop="genre"]/text()').extract_first()
        price = response.xpath('//button[@class="price buy id-track-click id-track-impression"]/span[2]/text()').extract_first()
        if price == u'Install': item["Price"] = 'free' 
        else: item["Price"] = price.split()[0]

        yield item

