from scrapy.crawler import CrawlerRunner
from twisted.internet import defer
from scrapy.utils.project import get_project_settings
import time
from twisted.internet import reactor

__author__ = 'dengjing'


if __name__ == '__main__':
    runner = CrawlerRunner(get_project_settings())

    @defer.inlineCallbacks
    def crawl():
        while True:
            yield runner.crawl('iqiyi')

    crawl()
    reactor.run()
