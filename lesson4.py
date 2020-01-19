import requests
from lxml import html
import time
from pymongo import MongoClient

class NewsGathererBase(object):
    site_base_url = None
    main_xpath_request = "//*"
    # headers = {
    #     "User-Agent": "URL/Emacs Emacs/26.1 (X11; x86_64-pc-linux-gnu)"
    # }

    def __init__(self):
        super(NewsGathererBase, self).__init__()
        self.res = []
        self.page = None

    def gather_news(self):
        with requests.get(self.site_base_url) as response:
            if not response.ok:
                raise RuntimeError('failed to get data from {}'.format(self.site_base_url))
            self.page = html.fromstring(response.text)
            self.process_page()

    def process_page(self):
        nodes = self.page.xpath(self.main_xpath_request)
        for node in nodes:
            self.res.append(self.postprocess(self.process_node(node)))

    def process_node(self, node):
        raise NotImplementedError

    def postprocess(self, news_data):
        return news_data.update('aggregator': self.site_base_url)


class MailRuNewsGather(NewsGathererBase):
    site_base_url = 'https://mail.ru/'
    main_xpath_request = "//div[contains(@class, 'news__list__item')]/a/span[contains(@class, 'text')]/.."

    def process_node(self, node):
        new_piece = {
            'url': node.get('href'),
            'heading': node.text_content()
        }
        return new_piece

    def postprocess(self, news_data):
        news_data = super(MailRuNewsGather, self).postprocess(news_data)
        with requests.get(news_data['url']) as response:
            if not response.ok:
                raise RuntimeError('failed to get data from {}'.format(news_data['url']))
            news_page = html.fromstring(response.text)
            date = news_page.xpath("//span[contains(@class, 'breadcrumbs__item')]/span/span/@datetime")
            source = news_page.xpath("//span[contains(@class, 'breadcrumbs__item')]/span/a/span/text()")
            news_data['source'] = source[0]
            news_data['date'] = date[0]
        return news_data


class LentaRuNewsGather(NewsGathererBase):
    site_base_url = 'https://lenta.ru/parts/news/'
    real_base_url = 'https://lenta.ru'
    main_xpath_request = "//div[contains(@class, 'news') and contains(@class, 'item')]"

    def process_node(self, node):
        if 'moslenta' in node[0][0].get('class'): # ignoring Moslenta news
            return {}
        ref_node = node[1][0][0]
        new_piece = {
            'url': self.real_base_url + ref_node.get('href'), # proper news have only relative urls
            'heading': ref_node.text,
            'source': node[0][0].text                         # source is another site section
        }
        return new_piece

    def postprocess(self, news_data):
        if len(news_data) == 0:
            return None
        news_data = super(LentaRuNewsGather, self).postprocess(news_data)
        time.sleep(1) # to get around retries amount
        with requests.get(news_data['url']) as response:
            if not response.ok:
                raise RuntimeError('failed to get data from {}'.format(news_data['url']))
            news_page = html.fromstring(response.text)
            date = news_page.xpath("//time[contains(@class, 'g-date')]/@datetime")
            news_data['date'] = date[0]
        return news_data

    def process_page(self):
        # here, loading of "next messages batch" is ignored
        super(LentaRuNewsGather, self).process_page()
        self.res = [r for r in self.res if r is not None]

crawler_types = [MailRuNewsGather, LentaRuNewsGather]
client = MongoClient('localhost', 27017)
db = client['news_database']
news = db.news

for ctype in crawler_types:
    crawler = ctype()
    crawler.gather_news()
    for n in crawler.res:
        res = news.insert_one(n)
        print('Inserted id:', res.inserted_id)
