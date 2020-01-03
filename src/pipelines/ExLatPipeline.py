# -*- coding: utf-8 -*-
import os
import json

from sqlalchemy import create_engine
from sqlalchemy.exc import DataError, IntegrityError, InvalidRequestError
from sqlalchemy.orm import Session
import requests

from items import ExLatItem
from helpers import mysql_connection_string


class ExLatPipeline(object):
    def __init__(self):
        self.engine = create_engine(mysql_connection_string())
        self.session = None

    def open_spider(self, spider):
        self.session = Session(self.engine)

    def process_item(self, item, spider):
        if isinstance(item, ExLatItem):
            icon = item['icon']
            thumbnail_image = item['thumbnail_image']
            title = item['title']
            title_symbol = item['title_symbol']
            price = item['price']
            currency = item['currency']
            currency_symbol = item['currency_symbol']
            whitepaper = item['whitepaper']
            long_description = item['long_description']
            website = item['website']
            facebook = item['facebook']
            linkedin = item['linkedin']
            telegram = item['telegram']
            twitter = item['twitter']
            video = item['video']
            video_image = item['video_image']

            data = {
                'icon': icon,
                'thumbnail_image': thumbnail_image,
                'title': title,
                'title_symbol': title_symbol,
                'price': price,
                'currency': currency,
                'currency_symbol': currency_symbol,
                'whitepaper': whitepaper,
                'long_description': long_description,
                'website': website,
                'facebook': facebook,
                'linkedin': linkedin,
                'telegram': telegram,
                'twitter': twitter,
                'video': video,
                'video_image': video_image,
                'project_type': 'ieo',
                'is_airdrop': 0,
            }

            # spider.logger.info(data)

            authorization_header = os.getenv("AUTHORIZATION_HEADER")

            headers = {
                'Content-Type': "application/json",
                'Authorization': authorization_header,
            }

            with open('api.txt', 'r') as f:
                api_url = f.read().strip()

            response = requests.request(
                "POST",
                api_url,
                data=json.dumps(data),
                headers=headers,
            )

            response = json.loads(response.text)

            if 'success' in response and response['success']:
                spider.logger.info('Success %s' % title)

            if 'error' in response and response['error']:
                spider.logger.info('Error %s' % title)
                spider.logger.info('Error: %s' % response['error'])

        return item

    def close_spider(self, spider):
        self.session.close()
