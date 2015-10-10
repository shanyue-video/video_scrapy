import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import tornado

__author__ = 'dengjing'


class CrawlIqiyi():

    def get(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl('iqiyi')
        process.start()


def run_scrapy():
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/iqiyi", CrawlIqiyi),
    ])
    return app


if __name__ == '__main__':
    run_scrapy().listen(int(sys.argv[1]), address='127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()