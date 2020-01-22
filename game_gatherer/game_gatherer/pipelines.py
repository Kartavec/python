# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo


class FillUrlPipeline(object):
    def process_item(self, item, spider):
        base_url = 'https://www.gog.com'
        processed = {
            'game_name': item['title'],
            'developer': item['developer'],
            'publisher': item['publisher'],
            'base_price': item['price']['baseAmount'],
            'final_price': item['price']['finalAmount'],
            'url': base_url + item['url']
        }
        return processed


class MongoPipeline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri='localhost',
            mongo_db='game_database'
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db.games2.insert(dict(item))
        return item
