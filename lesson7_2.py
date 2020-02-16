# mail box scrapping

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
# same database used
db = client['mail_db']
saved_books = db.books


driver = webdriver.Firefox()
scroll_pause = 3
wait = WebDriverWait(driver, scroll_pause)
# ozon top 200 books
driver.get('https://www.ozon.ru/highlight/22872/')

timeouts = 0

while timeouts < 5:
    print('scrolling...')
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    # time.sleep(scroll_pause)
    old_height = driver.execute_script("return document.body.scrollHeight")
    try:
        wait.until(lambda d: d.execute_script("return document.body.scrollHeight") > old_height)
        timeouts = 0
    except TimeoutException:
        print('timeout...')
        timeouts += 1

    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == old_height:
        print ('same height')
        timeouts += 1
    else:
        old_height = new_height
print('finished scrolling...')

base_url = 'https://www.ozon.ru'
soup = bs(driver.page_source, 'lxml')
list_book_tags = soup.findAll(attrs={'data-test-id':"tile-name"})
for book_tag in list_book_tags:
    # some variable reuse here
    title = book_tag.text.split('|')
    if len(title) > 1:
        author = title[1].strip()
    else:
        author = ''
    title = title[0].strip()
    url = base_url + book_tag['href']
    # ignoring discounts if there are any present
    price = book_tag.parent.find(attrs={'data-test-id':'tile-price'}).text
    print('Saving data on book ', url)
    saved_books.insert_one({
        'title': title,
        'url': url,
        'title': title,
        'price': price
    })

driver.quit()
