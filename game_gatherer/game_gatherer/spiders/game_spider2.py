# -*- coding: utf-8 -*-
import scrapy


class GameSpider2Spider(scrapy.Spider):
    name = 'game_spider2'
    start_urls = ['https://www.cdkeys.com/pc/games/']

    def parse(self, response):
        next_pages = response.xpath("//span[@class='pager']/div/ol/li[@class='next']/a/@href")
        if next_pages:
            for page in next_pages:
                break
                yield response.follow(page.extract(), callback=self.parse)
                # there are 2 pager elements with identical next page links
                break
        game_data = response.xpath("//div[@class='category-products custom_category']//a/div[@class='game-name']/../@href")
        for game in game_data:
            yield response.follow(game.extract(), callback=self.process_page)

    def process_page(self, response):
        res = {}
        res['url'] = response.url
        xp_title = response.xpath("//div[@class='product_content']/h1[@class='title' and @itemprop='name']/text()")
        res['game_name'] = xp_title[0].extract()
        xp_details = response.xpath("//div[@class='game_details']/div[@class='game_content']/dl/dd/text()")
        # print('publisher: ', xp_details[1].extract(), ' developer: ', xp_details[2].extract())
        res['developer'] = xp_details[1].extract()
        res['publisher'] = xp_details[2].extract()
        xp_price = response.xpath("//div[@class='product_price']/div/div/span[@class='rates']/meta[@itemprop='price']/@content")
        final_price = xp_price[0].extract()
        # price is expressed as $10 or something in text, with some regards to currently active currency
        # so we get price from metadata, and use it to isolate currency cymbol and get base price
        xp_price = response.xpath("//div[@class='product_price']/div/div/span[@class='rates']/span[@class='price']/text()")
        prefix = xp_price[0].extract()[:-len(final_price)]
        xp_price = response.xpath("//div[@class='product_price']/div/div/span[@class='rates']/span[@class='price_original']/span/text()")
        base_price = xp_price[0].extract()[len(prefix):]
        # print('prefix: ', prefix, ' base price: ', base_price, ' final price: ', final_price)
        res['base_price'] = base_price
        res['final_price'] = final_price
        res['currency'] = prefix.strip()
        yield res

