# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.loader.processors import Join, TakeFirst, Identity


class FrogscrapItem(scrapy.Item):
    _id = scrapy.Field()
    title = scrapy.Field(output_processor=TakeFirst())
    url = scrapy.Field()
    author = scrapy.Field(output_processor=TakeFirst())
    translator = scrapy.Field(output_processor=TakeFirst())
    book_img = scrapy.Field()
    text = scrapy.Field(output_processor=Join())
    cover = scrapy.Field(output_processor=TakeFirst())
    file_urls = scrapy.Field()
    files = scrapy.Field()

    def __repr__(self):
        return u'<item title: {}, url: {}, cover_url: {}>'.format(self['title'], self['url'], self['cover'])
