import requests
from lxml import html

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
                raise RuntimeError('failed to get data from {}'.format(self.site_base_url))
            news_page = html.fromstring(response.text)
            date = news_page.xpath("//span[contains(@class, 'breadcrumbs__item')]/span/span/@datetime")
            source = news_page.xpath("//span[contains(@class, 'breadcrumbs__item')]/span/a/span/text()")
            news_data['source'] = source[0]
            news_data['date'] = date[0]
        return news_data

