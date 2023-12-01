
import time
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup as bs


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')


ITEM_DATA_STRINGS = {
    "name": "'NAME':'",
    "article": "'ARTICLE_SEARCH':'",
    "price": "'VALUE_VAT':'",
    "amount": "'ACTUAL_WEIGHT':'"
}

def get_items_data(script):
    '''парсим строку, содержащую данные SKU'''
    counter = script.count("'ARTICLE_SEARCH':'")
    start = 0
    items = []
    items.append(_get_item_data(script, start, 'name')[0])
    for i in range(counter):
        item = {}
        item['price'], start = _get_item_data(script, start, 'price')
        item['amount'], _ = _get_item_data(script, start, 'amount')
        item['article'], _ = _get_item_data(script, start, 'article')
        items.append(item)
    return items


def _get_item_data(script, start, data_type):
    start = script.index(ITEM_DATA_STRINGS[data_type], start) \
        + len(ITEM_DATA_STRINGS[data_type])
    end = script.index("'", start)
    value = script[start:end]
    return value, start


def close_pop_up(driver):
    '''скрываем попап'''
    time.sleep(3)
    try:
        element = driver.find_elements(By.CLASS_NAME, "close")[0]
        element.click()
    except Exception as e:
        print(e)
        pass


def thread_parsing(URL):
    t = time.time()
    driver = webdriver.Chrome(options=chrome_options)
    driver.set_page_load_timeout(time_to_wait=10)

    try:
        driver.get(URL)
    except TimeoutException:
        driver.execute_script("window.stop();")
    
    select_city('Москва')
    source_data = driver.page_source
    parse_page(source_data)
    
    while True:
        try:
            element = driver.find_elements(By.CLASS_NAME, "nums")[0]
            driver.execute_script(
                "arguments[0].scrollIntoView(true);", 
                element
                )
            element = driver.find_elements(
                By.XPATH, "//div[@class='nums']//a[@class='flex-next']"
                )[0]
            url = element.get_attribute('href')
            try:
                driver.get(url)
            except TimeoutException:
                driver.execute_script("window.stop();")
            
            print('!!here')
            source_data = driver.page_source
            parse_page(source_data)
            # close_pop_up(driver)
            
        except:
            break


def parse_page(source_data):

    soup = bs(source_data,  "html.parser")

    scripts = soup.find_all('script')

    with open('result.txt', 'a', encoding='utf-8-sig') as f:
        for script in scripts:
            try:
                items = get_items_data(script.text)
                f.write(json.dumps(items, ensure_ascii=False) + "\n")
            except Exception as e:
                pass

    return


def get_subcategory_urls():
    # тут нужно парсить субкатегории, но пока просто хардкод в файле
    URLS = []
    with open('sub_urls.txt', 'r', encoding='utf-8-sig') as f:
        for line in f.readlines():
            URLS.append(line.strip())
    return URLS


def select_city(city):
    pass