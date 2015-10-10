import sys
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time
import tornado
import tornado.options
import tornado.web
import tornado.gen

__author__ = 'dengjing'


class CrawlIqiyi(tornado.web.RequestHandler):

    def get(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl('iqiyi')
        process.start()
        return

class Iqiyi(tornado.web.RequestHandler):

    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        crawl = CrawlIqiyi()
        while True:
            crawl.get()
            time.sleep(3000)
        self.finish()


def run_scrapy():
    tornado.options.parse_command_line()
    app = tornado.web.Application([
        (r"/crawl_iqiyi", CrawlIqiyi),
        (r"/iqiyi", Iqiyi),
    ])
    return app


if __name__ == '__main__':
    run_scrapy().listen(int(sys.argv[1]), address='127.0.0.1')
    tornado.ioloop.IOLoop.instance().start()