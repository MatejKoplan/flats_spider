import scrapy


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
