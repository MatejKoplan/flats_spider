import scrapy

from pathlib import Path

from spider.luxonis_crawler.spiders.helpers import url_discovery
from spider.luxonis_crawler.spiders.helpers import flats_extractor


class FlatsSpider(scrapy.Spider):
    name = "flats"

    def start_requests(self):
        urls = [
            "https://www.sreality.cz/en/search/for-sale/houses"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = url_discovery.extract_urls(response)
        flats = flats_extractor.extract_flats(response)
        # TODO:
        #  Save to DB

        #  Add sorted URLs to frontier
        for url in urls
            yield scrapy.Request(url, callback=self.parse)
