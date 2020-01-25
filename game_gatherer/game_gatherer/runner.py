from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from game_gatherer import settings
from game_gatherer.spiders.game_spider import GameSpider

if __name__ == '__main__':
    crawler_settings = Settings()
    crawler_settings.setmodule(settings)
    process = CrawlerProcess(settings=crawler_settings)
    process.crawl(GameSpider)
    process.start()
