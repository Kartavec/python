"""
1. Посмотреть документацию к API GitHub, разобраться как вывести список репозиториев для конкретного пользователя,
сохранить JSON-вывод в файле *.json.
"""

import requests
import json

def get_json(url: str) -> dict:
    """
    Получение json по url
    :param url: Ссылка
    :return:
    """
    response = requests.get(url)
    if response.status_code != 200:
        raise requests.ConnectionError
    return response.json()

USERNAME = 'eadevlab'
url = 'https://api.github.com/users/%s/repos' % USERNAME
try:
    repos_info = get_json(url)
    repo_names = [_['name'] for _ in repos_info ]
    with open('./repos.json', 'w') as f:
        json.dump(repo_names, f)
    print('Список репозиториев:', *repo_names, sep='\n')
except requests.ConnectionError:
    print('Возникла ошибка')