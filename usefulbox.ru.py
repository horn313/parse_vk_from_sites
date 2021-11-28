import random
import time

import requests
from bs4 import BeautifulSoup

page_number = 1
for page_number in range(1,85):
     try:
        link = f'https://usefulbox.ru/sadovod/page/{page_number}/'
        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')
        posts = soup.find('div', class_ = 'blog_posts')
        blog = posts.find_all('div', class_ = [
            'story post_preview cf vkg_ads_post vkg_ads_post_even vkg_ads_post_place',
            'story post_preview cf vkg_ads_post vkg_ads_post_odd vkg_ads_post_place',
            'story post_preview cf vkg_ads_post vkg_ads_post_even',
            'story post_preview cf vkg_ads_post vkg_ads_post_odd',
            'story post_preview cf'])
        for vk_block in blog:
            block = vk_block.find('div', class_ = 'thecl_table_col thecl_vk')
            vk_link = block.find('a').get('href')
            with open('userfulbox.txt','a') as file:
                file.write('\n'+vk_link)
        print(f'Обработал {page_number} страницу, осталось примерно {85-page_number} страниц')
        page_number += 1
        time.sleep(random.randrange(1,5))
     except:
        print(f'Не могу найти страницу {page_number}, я сворачиваюсь')
        break
print(f'All is ok, I found {page_number} pages and give you all info you need!')
