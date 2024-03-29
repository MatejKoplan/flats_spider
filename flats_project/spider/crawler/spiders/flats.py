import os
import scrapy
import logging

from scrapy_playwright.page import PageMethod
from typing import Generator

from db.models import Flat
from config import config


class FlatsSpider(scrapy.Spider):
    name = "flats"

    def start_requests(self):
        urls = [
            "https://www.sreality.cz/en/search/for-sale/houses"
        ]
        for url in urls:
            # Using scrapy.Request with Playwright meta instead of scrapy.FormRequest
            yield scrapy.Request(
                url=url,
                meta={
                    "playwright": True,
                    "playwright_include_page": True,
                    "playwright_page_methods": [
                        PageMethod("wait_for_selector", ".dir-property-list"),
                    ]
                },
                callback=self.parse
            )

    def parse(self, response: scrapy.http.Response, **kwargs) -> Generator[scrapy.Request, None, None]:
        # Extract possible new URLs and data from page
        urls = extract_urls(response)
        flats = extract_flats(response)
        logging.debug(f"found {len(flats)} flats")
        if flats:
            Flat.insert_flats_with_images(flats)
            logging.debug("inserted into db")
        elif config.ENVIRONMENT == config.DEVELOPMENT_ENV:
            # Save HTML to a file if no flats found
            filename = f"no_flats_found_{response.url.split('/')[-1]}.html"
            self.save_html(response.text, filename)
            logging.debug(f"Saved page HTML to {filename}")

        # Add sorted URLs to frontier
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    @staticmethod
    def save_html(html_content: str, filename: str) -> None:
        """ Save the HTML content to a file """

        file_path = os.path.join('/data', filename)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(html_content)


def extract_flats(response: scrapy.http.Response) -> list[Flat]:
    property_cards = response.css(".dir-property-list > .property")

    # We want to gather 500 items, there are 20 per page, so we should stop gathering on page 20.
    flats = []
    for property_card in property_cards:
        image_urls = property_card.css("a > img::attr(src)").getall()
        posting_name = property_card.css(".info.clear.ng-scope > div > span > h2 > a > span::text").get()
        flats.append(Flat(title=posting_name, images=image_urls))

    return flats


def extract_urls(response: scrapy.http.Response) -> list[str]:
    link_items = response.css(".paging-full > li > a")

    # We want to gather 500 items, there are 20 per page, so we should stop gathering on page 20.
    filtered_link_items = []
    for item in link_items:
        link_text = item.css("::text").get()
        if link_text and int(float(link_text)) <= (500 / 20):
            filtered_link_items.append(item)

    relative_urls = map(lambda link_tag: link_tag.css("::attr(href)").get(), filtered_link_items)
    absolute_urls = list(map(lambda relative_url: response.urljoin(relative_url), relative_urls))

    return absolute_urls
