import asyncio
import aiohttp
import requests
import time

from logger import logger

from bs4 import BeautifulSoup as bs


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/116.0',
}
URLS = [
    'https://www.google.com/search?q=%D1%81%D1%81%D1%81%D1%80',
    'https://www.google.com/search?q=%D1%81%D1%88%D0%B0',
    'https://www.google.com/search?q=%D0%BA%D0%B0%D0%BD%D0%B0%D0%B4%D0%B0',
]

async def parse_url(session, url):
    async with session.get(url) as r:
        soup = bs(await r.text(), 'html.parser')
        items = soup.find_all('div', class_='MjjYud')
        logger.warning(f'! len(items)')
        for item in items:
            title = item.find('h3', class_='LC20lb')
            if title:
                logger.warning(title.text)


async def main():
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        tasks = []
        for url in URLS:
            task = asyncio.create_task(parse_url(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)
        

if __name__ == '__main__':
    t1 = time.time()
    asyncio.run(main())
    logger.debug(time.time() - t1)

















# async def parse_page(session, url):
#     async with session.get(url) as r:
#         soup = bs(await r.text(), 'html.parser')
#         items = soup.find_all('div', class_='MjjYud')
#         logger.warning(f'! len(items)')
#         for item in items:
#             title = item.find('h3', class_='LC20lb')
#             if title:
#                 logger.warning(title.text)



# async def main():
#     async with aiohttp.ClientSession(headers=HEADERS) as session:
#         tasks = []
#         for url in URLS:
#             task = asyncio.create_task(parse_page(session, url))
#             tasks.append(task)

#         await asyncio.gather(*tasks)


# if __name__ == '__main__':
#     t1 = time.time()
#     asyncio.run(main())
#     print(time.time() - t1)

