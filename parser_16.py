import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.content


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    apartments = soup.find_all('div', class_='c-card')

    for apartment in apartments:
        link = apartment.find('div', class_='c-card__description').find('div', class_='c-card__container').find('div', class_='c-card__column-left').find('a').get('href')
        room = apartment.find('div', class_='c-card__description').find('div', class_='c-card__container').find('div', class_='c-card__column-left').find('a').text.strip()[0]
        all_address_r = apartment.find('div', class_='c-card__description').find('div', class_='c-card__container').find('div', class_='c-card__column-left').find('div', class_='c-card__addr').text.split(',')
        all_address = [i.strip() for i in all_address_r]
        address = ', '.join(all_address[1:])
        region = all_address[0]
        price_r = apartment.find('div', class_='c-card__description').find('div', class_='c-card__container').find('div', class_='c-card__column-right').find('div', class_='price data_price').text.split()
        price = int(int(''.join(price_r[:-1])) // 3.2)
        print(link, room, address, region, price, sep='\n')


for i in range(1, 6):
    url = f'https://neagent.by/kvartira/snyat?roomCount={i}'
    get_page_data(get_html(url))
    print(f'Работа завершена. Все новые {i} - комнатные квартиры найдены!')
