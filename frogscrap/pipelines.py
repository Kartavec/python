# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient
from scrapy.pipelines.files import FilesPipeline
import scrapy
from settings import COVERS_STORE


class FrogscrapPipeline(FilesPipeline):
    def get_media_requests(self, item, info):
        try:
            yield scrapy.Request(item['cover'])
        except Exception as e:
            print(e)

    def item_completed(self, results, item, info):
        if results:
            item['cover'] = results[0]
        return item

    def __init__(self, store_uri, *args, **kwargs):
        # change store for our custom setting
        super(FrogscrapPipeline, self).__init__(COVERS_STORE, *args, **kwargs)


class DataBasePipeline(object):
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongo_base = client.warpfrog

    def process_item(self, item, spider):
        collection = self.mongo_base['content']
        collection.insert_one(item)
        return item
