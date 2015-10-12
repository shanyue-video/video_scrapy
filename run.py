from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
import time
from twisted.internet import reactor

__author__ = 'dengjing'


if __name__ == '__main__':
    while True:
        runner = CrawlerRunner(get_project_settings())
        d = runner.crawl('iqiyi')
        d.addBoth(lambda _: reactor.stop())
        reactor.run()
        time.sleep(3)
