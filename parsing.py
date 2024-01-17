import threading
import asyncio
import aiohttp

from services import thread_parsing, get_subcategory_urls


async def parsing_main():
    
    URLS = get_subcategory_urls()
    
    threads = []
    for url in URLS:
        threads.append(threading.Thread(target=thread_parsing, args=(url,)))
        threads[-1].start()
    for thread in threads:
        thread.join()
    
           

if __name__ == '__main__':
    asyncio.run(parsing_main())