import requests
from bs4 import BeautifulSoup
import csv
import time


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('parsing_file4.csv', 'a', errors='ignore') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['link'], data['v'], data['year'], data['pro'], data['price']))


def res(p):
    return p.replace(' *', '')


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    sections = soup.find('div', class_='styles_cards__iNIi9').find_all('section')

    count = 1
    ost = len(sections)
    for section in sections:
        try:
            link = section.find('a', class_='styles_wrapper__eefVX').get('href')
        except AttributeError:
            link = '---'

        try:
            name = section.find('h3', class_='styles_title__A3M1R styles_ellipsis__xPYm_').text
        except AttributeError:
            name = '---'

        try:
            v = section.find('p', class_='styles_params__f_CvZ styles_ellipsis__xPYm_').text
        except AttributeError:
            v = '---'

        try:
            year = section.find('div', class_='styles_year__I2HyA').text
        except AttributeError:
            year = '---'

        try:
            pro = section.find('div', class_='styles_mileage___SUmz').text
        except AttributeError:
            pro = '---'

        try:
            p = section.find('div', class_='styles_price__PGuBm').find_all('span')[1].text
            price = res(p)
        except AttributeError:
            price = '---'

        data = {'name': name,
                'v': v,
                'year': year,
                'pro': pro,
                'price': price,
                'link': link}

        time.sleep(1)

        write_csv(data)

        print(f'Выполнено {count} итераций, осталось {ost - count} итераций')
        count += 1





def main():
    url = 'https://auto.kufar.by/l/kupit/motocikl?cur=BYR&prc=r%3A100000%2C100000000000&size=30&sort=lst.d'
    iteration = 1

    while True:
        get_page_data(get_html(url))

        soup = BeautifulSoup(get_html(url), 'lxml')

        try:
            url_link = soup.find('div', class_='styles_links__inner__huze7').find_all('a')
            url = 'https://auto.kufar.by' + url_link[-1].get('href')
        except AttributeError:
            break

        if len(url_link) < 5 and iteration != 1:
            break
        time.sleep(10)
        iteration += 1



if __name__ == '__main__':
    main()