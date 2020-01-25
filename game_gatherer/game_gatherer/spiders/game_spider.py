import scrapy
import json
import urllib

class GameSpider(scrapy.Spider):
    name = 'game'
    start_urls = [
        "https://www.gog.com/games"
    ]

    def make_page_url(self, page):
        base_url = "https://www.gog.com/games/ajax/filtered?"
        params = {
            'mediaType': 'game',
            'page': page
        }
        full_url = base_url + '&'.join('{}={}'.format(k, params[k]) for k in params.keys())
        return full_url

    def start_requests(self):
        target = self.make_page_url(1)
        yield scrapy.Request(url=target, callback=self.parse)

    def parse(self, response):
        jsonresponse = json.loads(response.body_as_unicode())
        current_page = jsonresponse['page']
        next_page = current_page + 1
        if next_page <= jsonresponse['totalPages']:
            yield response.follow(self.make_page_url(next_page), callback=self.parse)

        for product in jsonresponse['products']:
            yield product
        print("Processed page", current_page)
