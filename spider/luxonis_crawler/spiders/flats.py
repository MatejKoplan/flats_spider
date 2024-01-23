import scrapy


class Flat:
    name: str
    image_urls: list[str]

    def __init__(self, name: str, image_urls: list[str]):
        self.name = name
        self.image_urls = image_urls

    def save_to_db(self):
        pass


class FlatsSpider(scrapy.Spider):
    name = "flats"

    def start_requests(self):
        urls = [
            "https://www.sreality.cz/en/search/for-sale/houses"
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        urls = extract_urls(response)
        flats = extract_flats(response)
        # TODO:
        #  Save to DB

        #  Add sorted URLs to frontier
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)


def extract_flats(response: scrapy.http.Response) -> list[Flat]:
    property_cards = response.css(".dir-property-list > .property")

    # We want to gather 500 items, there are 20 per page, so we should stop gathering on page 20.
    flats = []
    for property_card in property_cards:
        image_urls = property_card.css("a > img::attr(src)").getall()
        posting_name = property_card.css(".info.clear.ng-scope > div > span > h2 > a > span::text").get()
        flats.append(Flat(name=posting_name, image_urls=image_urls))

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