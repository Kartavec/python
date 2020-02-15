# mail box scrapping

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from pymongo import MongoClient
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException

client = MongoClient('localhost', 27017)
db = client['mail_db']
saved_mails = db.mails

driver = webdriver.Firefox()
driver.implicitly_wait(10)

driver.get('https://passport.yandex.ru/auth?from=mail/')
# enter login
login_field = driver.find_element_by_id('passp-field-login')
login_field.send_keys('kurvivor19@yandex.ru', Keys.ENTER)
# enter password
wait = WebDriverWait(driver, 30, ignored_exceptions=[NoSuchElementException, StaleElementReferenceException])
next_wait = WebDriverWait(driver, 60, ignored_exceptions=[StaleElementReferenceException])
password_field = wait.until(lambda d : d.find_element_by_id('passp-field-passwd'))
# password_field = driver.find_element_by_id('passp-field-passwd')
password_field.send_keys('exodus', Keys.ENTER)

if 'auth/phone' in driver.current_url:
    skip_btn = driver.find_element_by_xpath("//div[@data-t='phone_skip']/button")
    skip_btn.click()

# wait until the auth completes
wait.until(lambda d : d.find_element_by_xpath("//div[@class='personal']"))

driver.get('https://mail.yandex.ru/')
# open first mail element
driver.find_element_by_xpath("//a[contains(@href, '#message')]").click()

while True:
    try:
        # we ignore distinction between formatted and plain emails and just get all text out
        mail_text = wait.until(lambda d: d.find_element_by_xpath("//div[contains(@class, 'mail-Message-Body-Content')]").text)
        mail_from = wait.until(lambda d: d.find_element_by_xpath("//div[@class='mail-Message-Sender']/span/span[@title]").text)
        mail_date = wait.until(lambda d: d.find_element_by_xpath("//div[@class='mail-Message-Sender']/following::div[contains(@data-key, 'message-head-date')]").text)
        mail_topic = wait.until(lambda d: d.find_element_by_xpath("//span[@class='mail-Message-Toolbar-Subject-Wrapper']/div").text)

        saved_mails.insert_one({
            'from': mail_from,
            'date': mail_date,
            'topic': mail_topic,
            'text': mail_text
        })

        try:
            next_wait.until(lambda d: d.find_element_by_xpath("//a[@data-direction='next']").click())
        except NoSuchElementException as e:
            break
    except TimeoutException as e:
        break

driver.quit()
