import requests
from bs4 import BeautifulSoup
import csv


def write_csv(data):
    with open('parsing_file5.csv', 'a', errors='ignore') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow((data['job_title'], data['job_code'], data['job_location'], data['job_description']))


def get_html(url):
    r = requests.get(url)
    return r.text


def format(item):
    text = ''
    for i in item:
        row = i.find('p').text
        text += row

    return text


def get_data2(html, number):
    soup = BeautifulSoup(html, 'lxml')

    id_dict = {1: {'job_title': 'comp-kp5wr51r', 'job_code': 'comp-kp5wr520', 'job_location': 'comp-kp5wr51w', 'job_description': 'comp-kp7bms9b'},
               2: {'job_title': 'comp-kp8gqjrc', 'job_code': 'comp-kp8gqjr6', 'job_location': 'comp-kp8gqjrn', 'job_description': 'comp-kp8gpelf'},
               3: {'job_title': 'comp-kp8gk4mw', 'job_code': 'comp-kp8gk4mo', 'job_location': 'comp-kp8gk4n8', 'job_description': 'comp-kp8gnf8m'},
               4: {'job_title': 'comp-kp8gx1g0', 'job_code': 'comp-kp8gx1fu', 'job_location': 'comp-kp8gx1gb', 'job_description': 'comp-kp8gui0d'},
               5: {'job_title': 'comp-kp8gx1g0', 'job_code': 'comp-kp8gx1fu', 'job_location': 'comp-kp8gx1gb', 'job_description': 'comp-kp8gui0d'},
               6: {'job_title': 'comp-kp8gy3qg', 'job_code': 'comp-kp8gy3qb', 'job_location': 'comp-kp8gy3qr', 'job_description': 'comp-kp8h4o8d'},
               7: {'job_title': 'comp-kxak17vr', 'job_code': 'comp-kxak17vi', 'job_location': 'comp-kxak17w8', 'job_description': 'comp-kxak2cvb'},
               8: {'job_title': 'comp-kp8gdchb', 'job_code': 'comp-kp8gdch5', 'job_location': 'comp-kp8gdchm', 'job_description': 'comp-kp8ggmu41'},
               9: {'job_title': 'comp-kp8hy9w3', 'job_code': 'comp-kp8hy9w1', 'job_location': 'comp-kp8hy9w7', 'job_description': 'comp-kp8i1fcs'},
               10: {'job_title': 'comp-kzrcke3h', 'job_code': 'comp-kzrcke3d', 'job_location': 'comp-kzrckdzl', 'job_description': 'comp-kzrd1iyk'},
               11: {'job_title': 'comp-l24vtzpb1', 'job_code': 'comp-l24vtzp91', 'job_location': 'comp-l24vtzmy', 'job_description': 'comp-l24vtznj'},
               12: {'job_title': 'comp-l51dekm4', 'job_code': 'comp-l51dekm21', 'job_location': 'comp-l51dekk1', 'job_description': 'comp-l51dekkj'},
               13: {'job_title': 'comp-l6drf7ov', 'job_code': 'comp-l6drf7op', 'job_location': 'comp-l6drf7p6', 'job_description': 'comp-l6drf7ps'}}

    category_dict = None
    if 0 <= number <= 22:
        category_dict = id_dict[1]
    elif 23 <= number <= 31:
        category_dict = id_dict[2]
    elif 32 <= number <= 37:
        category_dict = id_dict[3]
    elif 38 <= number <= 39:
        category_dict = id_dict[4]
    elif 40 <= number <= 41:
        category_dict = id_dict[5]
    elif 42 <= number <= 45:
        category_dict = id_dict[6]
    elif 46 <= number <= 64:
        category_dict = id_dict[7]
    elif 65 <= number <= 76:
        category_dict = id_dict[8]
    elif 77 <= number <= 87:
        category_dict = id_dict[9]
    elif 88 <= number <= 93:
        category_dict = id_dict[10]
    elif 94 <= number <= 95:
        category_dict = id_dict[11]
    elif 96 <= number <= 111:
        category_dict = id_dict[12]
    elif 112 <= number <= 113:
        category_dict = id_dict[13]

    try:
        job_title = soup.find('div', id=category_dict['job_title']).find('span').text
    except AttributeError:
        job_title = 'None'

    try:
        job_code = soup.find('div', id=category_dict['job_code']).find('span').text
    except AttributeError:
        job_code = 'None'

    try:
        job_location = 'Location: ' + soup.find('div', id=category_dict['job_location']).find('span').text
    except AttributeError:
        job_location = 'None'

    try:
        j = soup.find('div', id=category_dict['job_description']).find_all('li')
        job_description = format(j)
    except AttributeError:
        job_description = 'None'

    data = {'job_title': job_title,
            'job_code': job_code,
            'job_location': job_location,
            'job_description': job_description}

    write_csv(data)



def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    jobs = soup.find_all('div', class_='_1ozXL')

    links = []
    for item in jobs:
        links.append(item.find('a', class_='_1fbEI').get('href'))

    count = 0
    for link in links:
        get_data2(get_html(link), count)
        print(f'{count} link passed! ^_^')
        count += 1



def main():
    url = 'https://www.indiesemi.com/careers'
    get_data(get_html(url))


if __name__ == '__main__':
    main()