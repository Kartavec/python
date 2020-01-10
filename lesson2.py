import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import urllib
from selenium import webdriver

driver = webdriver.Firefox()
# headers = {
#     "User-Agent": "URL/Emacs Emacs/26.1 (X11; x86_64-pc-linux-gnu)",
#     "Accept-Language": "en",
#     "Accept-Charset": "utf-8"
# }

base_link = "https://www.gog.com"
main_link = base_link + "/games"

params = {
    'category': 'strategy',
    'sort': 'popularity',
    'page': 1
}

categories = [
    'strategy',
    'simulation',
    'indie',
    'racing',
    'action',
    'strategy',
    'shooter',
    'adventure'
]

# response = requests.request('GET', main_link, headers=headers, params=params)
# soup = bs(response.text, 'lxml')

df = pd.DataFrame(columns=['name', 'store_page', 'full_price', 'discount', 'final_price', 'category'])


def process_games_page(url, frame, category):
    driver.get(url)
    soup = bs(driver.page_source, 'lxml')
    game_list_tag = soup.find(attrs={'class':"catalog__games-list"})
    if game_list_tag is None:
        return None
    game_list = game_list_tag.select('.product-tile')
    if not game_list:
        return None
    for game in game_list:
        link_tag = game.findChild('a')
        if not link_tag.has_attr('href'):
            continue
        game_link = base_link + link_tag['href']
        title_tag = link_tag.findChild('div', {'class': 'product-tile__title'})
        game_title = title_tag.text
        prices_tag = link_tag.findChild('div', {'class': 'product-tile__prices'})
        discount = ''
        discount_tag = prices_tag.select('.product-tile__discount')
        if discount_tag:
            discount = discount_tag[0].text
        final_tag = prices_tag.select('.product-tile__price-discounted._price')[0]
        final_price = int(final_tag.text)
        full_price = final_price
        full_tag = prices_tag.select('.product-tile__price')
        if full_tag:
            full_price = int(full_tag[0].text)
        frame = frame.append({'name': game_title,
                              'store_page': game_link,
                              'full_price': full_price,
                              'discount': discount,
                              'final_price': final_price,
                              'category': category
        }, ignore_index=True)
    return frame

for cat in categories:
    params['category'] = cat
    for page in range(1, 10):
        params['page'] = page
        request_link = main_link + '?' + urllib.urlencode(params)
        next_frame = process_games_page(request_link, df, cat)
        if next_frame is not None:
            df = next_frame
        else:
            break

print('In collected dataframe:', df.shape[0], 'games')
df.to_csv('gog_games.csv', encoding='utf-8')
