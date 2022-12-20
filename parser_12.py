import requests
import csv
from bs4 import BeautifulSoup


def get_html(url):
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0'}
    r = requests.get(url, headers=user_agent)
    return r.text


def write_csv(data):
    with open('parsing_file9.csv', 'a', errors='ignore') as file:
        order = ['author', 'since']
        writer = csv.DictWriter(file, delimiter=';', fieldnames=order)
        writer.writerow(data)


def get_articles(html):
    soup = BeautifulSoup(html, 'lxml')
    ts = soup.find('div', class_='testimonial-container').find_all('article')
    return ts


def get_page_data(ts):
    for item in ts:
        try:
            since = item.find('p', class_='traxer-since').text.strip()
        except:
            since = '---'
        try:
            author = item.find('p', class_='testimonial-author').text.strip()
        except:
            author = '---'
        data = {'author': author, 'since': since}

        write_csv(data)


def main():
    page = 1
    while True:
        url = f'https://catertrax.com/traxers/page/{str(page)}/'

        articles = get_articles(get_html(url))
        if articles:
            get_page_data(articles)
            print(f'Page {page} done!')
            page += 1
        else:
            break


if __name__ == '__main__':
    main()