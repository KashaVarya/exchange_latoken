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
    video = scrapy.Field()
    video_image = scrapy.Field()

    # facebook, linkedin, telegram, twitter
    # project_type всегде ieo
    # is_airdrop всегда 0

    short_description = scrapy.Field()
    restricted_areas = scrapy.Field()
    pre_sale_start_date = scrapy.Field()
    pre_sale_end_date = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
