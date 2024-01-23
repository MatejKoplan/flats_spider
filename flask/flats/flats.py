class Flat:
    name: str
    image_urls: list[str]

    def __init__(self, name: str, image_urls: list[str]):
        self.name = name
        self.image_urls = image_urls


    def load_from_db(self):
