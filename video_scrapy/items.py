# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideoScrapyItem(scrapy.Item):
    video_title = scrapy.Field()
    video_source_url = scrapy.Field()
    video_publish_time = scrapy.Field()
    video_author = scrapy.Field()
