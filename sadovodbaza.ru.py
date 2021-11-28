import requests
import fake_useragent
from bs4 import BeautifulSoup

page_number = 1
while page_number < 110:
    try:
        print(f'Обработатываю {page_number} страницу, осталось примерно {110-page_number} страниц')
        link = f'https://sadovodbaza.ru/page/{page_number}/'
        responce = requests.get(link).text
        soup = BeautifulSoup(responce, 'lxml')
        block = soup.find('div', id = 'post-list')
        article = block.find_all('span', class_='icon-soc')
        for i in article:
            vk_link = i.find('a').get('href')
            with open('тест', 'a') as file:
                file.write('\n'+vk_link)
        print(f'Страница {page_number} обработана')

        page_number +=1
    except:
        print(f'Не могу прочитать {page_number} страницу, я сворачиваюсь!')
        break

print(f'All is ok! In result I read {page_number} pages and save all information you need')
