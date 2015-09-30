# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
# from video_scrapy.settings import MONGODB_SERVER
# from video_scrapy.settings import MONGODB_USER
# from video_scrapy.settings import MONGODB_PORT
# from video_scrapy.settings import MONGODB_PASSWORD


class VideoScrapyPipeline(object):

    def __init__(self):
        # client = MongoClient('mongodb://'+ MONGODB_USER + ':' + MONGODB_PASSWORD + '@' + MONGODB_SERVER, MONGODB_PORT)
        db = MongoClient('123.57.6.46')
        # client = MongoClient('mongodb://123.57.6.46:27017/')
        # client = MongoClient('mongodb://root:dengjing@123.57.6.46:27017/')
        db.video_scrapy.authenticate("scrapy", "123456")
        # db = client.database
        # self.collection = client.collection
        print('!!!!!!!!', db.video_scrapy.base_video.find_one())
        pass

    def process_item(self, item, spider):
        print('--------收录视屏-------')
        print item['video_title']
        print item['video_source_url']
        print item['video_publish_time']
        print item['video_author']
        return item
