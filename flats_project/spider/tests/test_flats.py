import scrapy
import json

from flats_project.spider.crawler.spiders import flats
from flats_project.db.models import Flat
from flats_project.db import models


def load_test_data(filename: str):
    data_file_path = 'spider/tests/data/' + filename
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
    flats_dict = list(map(lambda flat: (flat.title, [image.url for image in flat.images]), found_flats))
    assert json.dumps(flats_dict) == json.dumps(expected_result)


def test_data_saving_and_loading():
    house_title = "House 1"

    image_urls = ["https://d18-a.sdn.cz/d_18/c_img_QO_K7/YdFBbqR.jpeg?fl=res,400,300,3|shr,,20|jpg,90", "https://d18-a.sdn.cz/d_18/c_img_QR_MK/rPfBbt8.jpeg?fl=res,400,300,3|shr,,20|jpg,90"]
    flat = Flat(title=house_title, images=image_urls)
    Flat.insert_flats_with_images([flat])

    with models.session_scope() as session:
        loaded_flats = Flat.load_all_flats(session)
        assert len(loaded_flats) == 1
        assert loaded_flats[0].title == house_title
        assert len(loaded_flats[0].images) == 2
        assert loaded_flats[0].images[0].url == image_urls[0]
