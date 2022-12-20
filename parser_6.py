import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def refined(s):
    r = [i for i in s if i.isdigit()]
    return ''.join(r)


def write_csv(data):
    with open('parsing_file2.csv', 'a') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['name'], data['url'], data['rating']))


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')

    for plugin in plugins:
        name = plugin.find('h3').text
        url = plugin.find('h3').find('a').get('href')

        r = plugin.find('span', class_='rating-count').find('a').text
        rating = refined(r)

        data = {'name': name,
                'url': url,
                'rating': rating}

        write_csv(data)


def main():
    url = 'https://ru.wordpress.org/plugins/'
    get_data(get_html(url))


if __name__ == '__main__':
    main()