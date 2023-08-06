import requests
from bs4 import BeautifulSoup


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0'
    }
    r = requests.get(url, headers=headers)
    if r.ok:
        return r.text
    print(r.status_code)


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')
    print(soup)
    apartments = soup.find('div', class_='classifieds-list').find_all('a', class_='classified')
    for apartment in apartments[:1]:
        # print(apartment)
        try:
            link = apartment.find('a', class_='classified').get('href')
        except AttributeError:
            link = ''
        print(link, '+')

        # try:
        #     room =
        # except AttributeError:
        #     room = None
        #
        # try:
        #     address =
        # except AttributeError:
        #     address = ''
        #
        # try:
        #     price =
        # except AttributeError:
        #     price = None


def main():
    url = 'https://r.onliner.by/ak/?rent_type%5B%5D=1_room&rent_type%5B%5D=2_rooms&rent_type%5B%5D=3_rooms&rent_type%5B%5D=4_rooms&rent_type%5B%5D=5_rooms&rent_type%5B%5D=6_rooms&only_owner=true#bounds%5Blb%5D%5Blat%5D=53.81901896704195&bounds%5Blb%5D%5Blong%5D=27.33531995648369&bounds%5Brt%5D%5Blat%5D=53.97681121698969&bounds%5Brt%5D%5Blong%5D=27.789617278027972'

    get_page_data(get_html(url))

if __name__ == '__main__':
    main()