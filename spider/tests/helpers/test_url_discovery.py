import scrapy
import json

from spider.luxonis_crawler.spiders.helpers import url_discovery


def test_url_discovery():
    data_file_path = 'spider/tests/helpers/data/test_url_discovery.json'
    with open(data_file_path, 'r') as file:
        data = json.load(file)

    expected = data["expected"]
    response = scrapy.http.HtmlResponse(url="https://www.sreality.cz/en/search/for-sale/houses",
                                        encoding="utf-8",
                                        body=data["input"])

    res = url_discovery.extract_urls(response)
    assert res == expected