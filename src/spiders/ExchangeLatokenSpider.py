# -*- coding: utf-8 -*-
import scrapy


class ExchangeLatokenSpider(scrapy.Spider):
    name = "exchange_latoken"

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(ExchangeLatokenSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=scrapy.signals.spider_closed)
        return spider

    def __init__(self, *args, **kwargs):
        scrapy.Spider.__init__(self, *args, **kwargs)

    def start_requests(self):
        return []

    def parse(self, response):
        pass

    def spider_closed(self):
        pass
