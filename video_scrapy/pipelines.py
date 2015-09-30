# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from video_scrapy.settings import MONGODB_SERVER
from video_scrapy.settings import MONGODB_USER
from video_scrapy.settings import MONGODB_PORT
from video_scrapy.settings import MONGODB_PASSWORD


class VideoScrapyPipeline(object):

    def __init__(self):
        # client = MongoClient('mongodb://'+ MONGODB_USER + ':' + MONGODB_PASSWORD + '@' + MONGODB_SERVER, MONGODB_PORT)
        # client = MongoClient('mongodb://root:dengjing@oforever.net:27017/video_scrapy')
        client = MongoClient('mongodb://root:dengjing@123.57.6.46:27017/')
        client.database.authenticate("root", "dengjing")
        db = client.database
        self.collection = db.collection

    def process_item(self, item, spider):
        print('--------收录视屏-------')
        print item['video_title']
        print item['video_source_url']
        print item['video_publish_time']
        print item['video_author']
        return item
