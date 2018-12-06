# -*- coding: utf-8 -*-
import scrapy
from newsCrawler.items import NewscrawlerItem
import re

class KompasSpider(scrapy.Spider):
    name = 'kompas'
    allowed_domains = ['kompas.com']
    start_urls = ['https://edukasi.kompas.com/indeks']

    for i in range(2, 10): # range of page to be crawl
        start_urls.append("https://edukasi.kompas.com/indeks"+str(i)+"")

    def parse(self, response):
        for href in response.css("a.article__link::attr(href)"):
            url = href.extract()
            yield scrapy.Request(url, callback=self.parse_contents)

    def parse_contents(self, response):
        item = NewscrawlerItem()
        item['url'] = response.url
        item['title'] = response.css('h1.read__title::text').extract_first()
        item['date'] = response.css('.read__time::text').extract_first().\
            strip('KOMPAS.com - ')
        item['author'] = response.css('.read__author a::text').extract_first()
        item['tag'] = response.css('a.tag__article__link::text').extract()
        item['desc'] = response.css('.read__content p::text, \
            a.inner-link-tag::text, em::text, strong::text').extract()
        yield item
