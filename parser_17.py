import csv
import requests
from bs4 import BeautifulSoup
import re


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.content


def write_to_csv_data(data, file_name: str):
    with open(f'{file_name.replace(" ", "_")}.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['price'], data['link']))


def number(text):
    list_num = re.findall(r'\d *\d+', text)
    str_num = ''.join(x for x in list_num[0] if x.isdigit())
    return int(str_num)


def get_page_data(html, product_name: str, exception_words: list):
    soup = BeautifulSoup(html, 'lxml')
    phones = soup.find_all('div', class_='css-1sw7q4x')
    summa, count = 0, 0

    for phone in phones:
        try:
            link = 'https://www.olx.pl' + phone.find('a').get('href')
        except AttributeError:
            continue
        try:
            name = phone.find('h6', class_='css-16v5mdi er34gjf0').text
        except AttributeError:
            continue
        try:
            price = number(phone.find('p', class_='css-10b0gli er34gjf0').text)
        except AttributeError:
            continue

        if product_name in name.lower() and not any([x for x in exception_words if x in name.lower()]):
            data = {'link': link,
                    'price': price,
                    'name': name}
            write_to_csv_data(data, product_name)
            summa += price
            count += 1

    print('Работа завершена, страница обработана!')
    return [summa, count]


def main(thing_name: str):
    page = 1
    summa, things = 0, 0

    while page < 2:
        url = f'https://www.olx.pl/elektronika/telefony/smartfony-telefony-komorkowe/warszawa/q-{thing_name.replace(" ", "-")}/?page={page}&search%5Bdist%5D=10&search%5Bfilter_enum_state%5D%5B0%5D=used&search%5Bfilter_float_price%3Afrom%5D=1000'
        print(f'Страница номер {page} обрабатывается ...')
        page += 1
        html = get_html(url)
        if html:
            info = get_page_data(html, product_name=thing_name, exception_words=['pro', 'mini', '256', '64', '512'])
            summa += info[0]
            things += info[1]
        else:
            print('Страница заблокирована, проверь статус ответа!')
            break

    average_price = summa / things
    return average_price


if __name__ == '__main__':
    print(main('iphone 14'))
