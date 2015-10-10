from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

__author__ = 'dengjing'


class manage:

    def run(self):
        process = CrawlerProcess(get_project_settings())
        process.crawl('iqiyi')
        process.start()


if __name__ == '__main__':
    manage = manage()
    manage.run()
