import threading

from services import thread_parsing, get_subcategory_urls


def parsing_main():
    
    URLS = get_subcategory_urls()
    
    threads = []

    for url in URLS:
        threads.append(threading.Thread(target=thread_parsing, kwargs={'URL':url}))
        threads[-1].start()
    for t in threads:
        t.join()
           

if __name__ == '__main__':
    parsing_main()