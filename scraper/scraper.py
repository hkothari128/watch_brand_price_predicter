from bs4 import BeautifulSoup
import csv
import re
import requests
import time
from tqdm import tqdm

from webdriver import get_webdriver

driver = get_webdriver()

BRANDS = [
    "iwc",
    "rolex",
    "movado",
    "nomos",
    "audemarspiguet",
    "breitling",
    "omega",
    "cartier",
    "patekphilippe",
    "gucci",
    "seiko",
    "zenith"
]
PAGE_COUNT = 5
HEADERS = ["Name","Brand","image","price"]

with open('watches.csv','w') as f:
    writer = csv.DictWriter(f, fieldnames=HEADERS)
    writer.writeheader
    for brand in tqdm(BRANDS):
        base_url = 'https://www.chrono24.com/{brand}/'.format(brand=brand)
        urls = [base_url] + [base_url+'index-{page}.htm'.format(page=i) for i in range(2,PAGE_COUNT+1)]
        print(brand,"\n")
        for url in urls:
            print(url)
            driver.get(url)
            time.sleep(2)
            for _ in range(15):
                javaScript = "window.scrollBy(0,1000);"
                driver.execute_script(javaScript)
                time.sleep(1)
            count = 0

            watches = driver.find_elements_by_css_selector('div .article-item-container')
            # print(watches[0].get_attribute('innerHTML'))
            
            for watch in tqdm(watches):
                try:
                    title = watch.find_element_by_css_selector('.article-title').get_attribute('innerText')
                    # print(title)
                    img = watch.find_element_by_css_selector('.article-image-container .content img').get_attribute('src')
                    # print(img)
                    if img.startswith('data'):
                        print(img,"XXXXXXXXXXXX")
                        break
                        img = None
                    # img = img if img.startswith('http') else None
                    price = watch.find_element_by_css_selector('.article-price div strong').get_attribute('innerText')
                    price = float(re.sub('[^0-9]*','',price))
                    # print(price)
                except:
                    print('skipped')
                if title and img and price:
                    writer.writerow({'Name':title ,'Brand':brand, 'image':img, 'price':price})
                    count += 1
                else:
                    print(title, img, price)
            print(count ," watches added")

    driver.quit()
            # page = requests.get(url)
            # soup = BeautifulSoup(page.content, 'html.parser')
            # # print(page.url, "URL")

            # watches = soup.select('div .article-item-container')
            # print(len(watches))
            # # imgs = soup.select('div .article-image-container .content')
            
            
            # print(watches[0])
            # imgs = [watch.select_one('.article-image-container .content img')['src'] for watch in watches]
            # print(imgs[0])
            # prices = [watch.select_one('.article-price div strong').find_all(text=True)[-1] for watch in watches]
            # print(prices[0])
        
            
        