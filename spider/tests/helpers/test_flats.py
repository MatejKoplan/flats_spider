import scrapy
import json

from spider.luxonis_crawler.spiders import flats


def load_test_data(filename: str):
    data_file_path = 'spider/tests/helpers/data/' + filename
    with open(data_file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)

    return data["input"], data["expected"]


def test_url_discovery():
    input_data, expected_result = load_test_data("test_url_discovery.json")

    response = scrapy.http.HtmlResponse(url="https://www.sreality.cz/en/search/for-sale/houses",
                                        encoding="utf-8",
                                        body=input_data)

    found_urls = flats.extract_urls(response)
    assert found_urls == expected_result


def test_flats_extraction():
    input_data, expected_result = load_test_data("test_flats_extraction.json")

    response = scrapy.http.HtmlResponse(url="https://www.sreality.cz/en/search/for-sale/houses",
                                        encoding="utf-8",
                                        body=input_data)

    found_flats = flats.extract_flats(response)
    assert found_flats == expected_result
