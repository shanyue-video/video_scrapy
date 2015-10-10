# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
import time
from video_scrapy.settings import MONGODB_HOST
from video_scrapy.settings import MONGODB_USER
from video_scrapy.settings import MONGODB_PASSWORD


class VideoScrapyPipeline(object):

    def __init__(self):
        db = MongoClient(MONGODB_HOST)
        db.video_scrapy.authenticate(MONGODB_USER, MONGODB_PASSWORD)
        self.db = db.video_scrapy.base_video

    def process_item(self, item, spider):
        print(time.strftime('%Y-%m-%d %H:%M:%S') + '--------收录视屏-------')
        item['spider'] = spider.name
        item['ctime'] = time.strftime('%Y-%m-%d %H:%M:%S')
        print(item)
        self.db.insert(dict(item))
        return item
