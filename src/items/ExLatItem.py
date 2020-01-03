# -*- coding: utf-8 -*-
import scrapy


class ExLatItem(scrapy.Item):
    icon = scrapy.Field()
    thumbnail_image = scrapy.Field()
    title = scrapy.Field()
    title_symbol = scrapy.Field()
    price = scrapy.Field()
    currency = scrapy.Field()
    currency_symbol = scrapy.Field()
    whitepaper = scrapy.Field()
    long_description = scrapy.Field()
    website = scrapy.Field()
    facebook = scrapy.Field()
    linkedin = scrapy.Field()
    telegram = scrapy.Field()
    twitter = scrapy.Field()
    video = scrapy.Field()
    video_image = scrapy.Field()
