"""
2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis).
Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию.
Ответ сервера записать в файл.
"""
from urllib.parse import urlencode
import requests
import json

class ApiClient:
    base_url = 'https://api.thecatapi.com/v1/'
    def __init__(self, api_key):
        """
        Конструктор
        :param api_key: Ключ доступа к апи
        """
        self.api_key = api_key

    def search(self,page:int=1,limit:int=10) -> dict:
        """
        Постраничный поиск фото
        https://api.thecatapi.com/v1/images/search?limit=&page
        :param page:
        :param limit:
        :return:
        """
        return self.__send('images/search', {
            'limit': limit,
            'page': page
        })

    def __send(self, method, params):
        """
        Отправка API запроса
        :param method:
        :param params:
        :return:
        """
        url = self.__build(method, params)
        response = requests.get(url)
        if response.status_code != 200:
            raise requests.ConnectionError
        return response.json()

    def __build(self, method, params):
        """
        Построение ссылки
        :param method:
        :param params:
        :return:
        """
        params['api_key'] = self.api_key
        return self.base_url+method+'?'+urlencode(params)


API_KEY = 'live_oNsVsaL8TAcRbmZzJvaWrPK0KJUlaVSF1Gu90EQ4Ldj1sJPirxXrFx8VhpaGwhaz'
client = ApiClient(API_KEY)
try:
    with open('./out.json','w') as f:
        json.dump(client.search(), f)
    print('Готово')
except requests.ConnectionError:
    print('Ошибка!')