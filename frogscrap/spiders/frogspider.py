# -*- coding: utf-8 -*-
import scrapy
import urllib
from frogscrap.items import FrogscrapItem
from scrapy.loader import ItemLoader
from pprint import pprint

class FrogspiderSpider(scrapy.Spider):
    name = 'frogspider'
    start_urls = ['https://wiki.warpfrog.wtf/index.php?title=%D0%A1%D0%BB%D1%83%D0%B6%D0%B5%D0%B1%D0%BD%D0%B0%D1%8F:%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D0%B8/']
    base_url = 'https://wiki.warpfrog.wtf'

    def parse(self, response):
        xp_next_link = response.xpath("//a[@rel='next']/@href")
        if xp_next_link:
            yield response.follow(xp_next_link[0].extract(), callback=self.parse)
        # print(urllib.unquote(response.url))
        xp_cat_links = response.xpath("//div[@id='mw-content-text']/div/ul/li/a/@href")
        for xp_cat_link in xp_cat_links:
            cat_url = self.base_url + xp_cat_link.extract()
            yield response.follow(cat_url, callback=self.process_cat)

    def process_cat(self, response):
        # print(urllib.unquote(response.url))
        xp_pages = response.xpath("//div[@id='mw-pages']/div/div/div/ul/li/a/@href")
        for xp_page in xp_pages:
            page_url = self.base_url + xp_page.extract()
            # print(urllib.unquote(page_url))
            yield response.follow(page_url, callback=self.process_page)

    def process_page(self, response):
        item = FrogscrapItem()
        loader = ItemLoader(item=FrogscrapItem(), response=response)
        loader.add_value('url', response.url)
        loader.add_value('file_urls', [response.url + '&action=mpdf'])
        loader.add_xpath('title', u"//h1[@id='firstHeading']/text()")
        loader.add_xpath('author', u"//div[@id='mw-content-text']/div/table/tbody/tr[3]/td[2]//text()")
        loader.add_xpath('translator', u"//div[@id='mw-content-text']/div/table/tbody/tr[4]/td[2]//text()")
        loader.add_xpath('text', u"//div[@id='mw-content-text']/div/h2//text() | //div[@id='mw-content-text']/div/h3//text() | //div[@id='mw-content-text']/div/p//text()")
        # pprint(loader.load_item())

        xp_image_url = response.xpath(u"//div[@id='mw-content-text']/div/table/tbody/tr[2]/td/div/div/a/@href")
        image_url = self.base_url + xp_image_url[0].extract()
        yield response.follow(image_url, callback=self.process_image, meta={'loader': loader})

    def process_image(self, response):
        loader = response.meta['loader']
        image_url = response.xpath("//div[@class='fullMedia']/p/a[@class='internal']/@href")
        # print (image_url[0].extract())
        loader.add_value('cover', self.base_url + image_url[0].extract())
        yield loader.load_item()
