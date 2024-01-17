import asyncio
import aiohttp
import requests

from bs4 import BeautifulSoup as bs

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
}
URLS = [
    'https://www.ozon.ru/category/muzhskaya-odezhda-7542/',
    'https://www.ozon.ru/category/mokasiny-i-topsaydery-muzhskie-7662/',
    'https://www.ozon.ru/category/muzhskie-topsaydery/',
]

for url in URLS:
    r = requests.get(url, headers=HEADERS)
    print(r)
    soup = bs(r.text, 'html.parser')
    items = soup.find_all('div', class_='v4i vi5')
    
    for item in items:
        print(item)
        price = item.find('c3118-a1 tsHeadline500Medium c3118-b9').text