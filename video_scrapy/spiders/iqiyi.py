# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule, Request
from video_scrapy.items import VideoScrapyItem


class IqiyiSpider(CrawlSpider):
    name = 'iqiyi'
    allowed_domains = ['iqiyi.com']
    start_urls = ['http://news.iqiyi.com/']

    rules = (
        Rule(LinkExtractor(allow=r'www/\d+/-------------4-1-2--1-.html'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(allow=r'www/\d+/-------------.*.html'), callback='parse_item', follow=True),
    )

    def parse_detail_item(self, response):
        # print('detail: ', response.url)
        i = VideoScrapyItem()
        i['video_title'] = response.xpath('//*[@id="widget-videotitle"]/text()').extract()[0]
        i['video_source_url'] = response.url
        i['video_publish_time'] = response.xpath('//*[@id="widget-vshort-ptime"]/text()').extract()[0]
        i['video_author'] = response.xpath('//*[@id="widget-vshort-un"]/text()').extract()[0]
        return i


    def parse_item(self, response):
        urls = response.xpath('//*/div[@class="site-piclist_pic"]/a/@href').extract()
        for url in urls:
            yield Request(url, callback=self.parse_detail_item)
        # return
        # i = VideoScrapyItem()
        # i['video_source_url'] = response.url
        # return i
        # print(response)
        # hxs = HtmlXPathSelector(response)
        # print(dir(response))
        # print(urls)
        # for url in urls:
        # yield Request(url)
        # i = VideoScrapyItem()
        # i['video_source_url'] = response.url
        # yield i
