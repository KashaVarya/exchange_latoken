from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from spiders import ExchangeLatokenSpider

process = CrawlerProcess(get_project_settings())

process.crawl(ExchangeLatokenSpider)
process.start()
