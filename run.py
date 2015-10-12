from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
import time

__author__ = 'dengjing'


class manage:

    def run(self):
        process = CrawlerProcess(get_project_settings())
        while True:
            process.crawl('iqiyi')
            process.start()
            time.sleep(3000)


if __name__ == '__main__':
    manage = manage()
    manage.run()
