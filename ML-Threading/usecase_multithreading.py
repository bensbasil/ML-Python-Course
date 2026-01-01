
'''
Real-World Example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping
Webscraping often involves making numerous network requests to fetch webpages. These tasks are I-O bound because they spend a lot of time waiting for responses from servers.
Multithreading can significantly improve the performance by allowing multiple pages to be fetched concurrently.
'''


'''
https://python.langchain.com/v0.2/docs/introduction/

https://python.langchain.com/v0.2/docs/concepts/

https://python.langchain.com/v0.2/docs/tutorials/

'''

import threading
import requests
from bs4 import BeautifulSoup

urls=[
'https://emojipedia.org/beans',

'https://www.searchhounds.com/articles/streaming-live-sports-events-2025.html?psystem=PW&domain=ilum.xyz',

'https://www.trybeans.com/integrations/trellis:facebook'

]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {len(soup.text)} characters from {url}')
          
threads=[]

for url in urls:
    thread=threading.Thread(target=fetch_content,args=(url,))
    threads.append(thread)
    thread.start()


for thread in threads:
    thread.join()

print("All Web pages fetched")