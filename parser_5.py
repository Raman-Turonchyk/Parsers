import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    return r.text


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    tag_p = soup.find('div', class_='site-branding').find('p', class_='site-title')
    return tag_p.text


def main():
    url = 'https://pl.wordpress.org/'
    print(get_data(get_html(url)))



if __name__ == '__main__':
    main()