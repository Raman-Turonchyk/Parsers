import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open('parsing_file3.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['url'], data['price']))


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table', class_='h7vnx2-2 cgeQEz cmc-table').find('tbody').find_all('tr')

    count = 0
    for tr in trs:
        tds = tr.find_all('td')
        try:
            name = tds[2].find('div', class_='sc-1prm8qw-0 pbu8wv-1 jDuhZQ name-area').find('p').text
            print(f'Операция {count} выполнена!')
        except AttributeError:
            pass
        try:
            name = tds[2].find('a').find_all('span')[1].text
            print(f'Операция {count} выполнена!')
        except (AttributeError, IndexError):
            pass
        url = 'https://coinmarketcap.com' + tds[2].find('a').get('href')
        price = tds[3].find('span').text.replace(',', '')

        data = {'name': name,
                'url': url,
                'price': price}

        write_csv(data)

        count += 1


def main():
    url = 'https://coinmarketcap.com'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()

