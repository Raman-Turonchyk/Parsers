import requests
import csv


def write_csv(data):
    with open('parsing_file7.csv', 'a', errors='ignore') as file:
        order = ['name', 'url', 'description', 'traffic', 'percent']
        writer = csv.DictWriter(file, delimiter=';', fieldnames=order)
        writer.writerow(data)


def get_html(url):
    r = requests.get(url)
    return r.text


def main():

    for i in range(1, 5078):
        url = f'https://www.liveinternet.ru/rating/ru//today.tsv?page={str(i)}'
        response = get_html(url)
        data = response.strip().split('\n')[1:]

        for row in data:
            columns = row.strip(). split('\t')
            name = columns[0]
            url = columns[1]
            description = columns[2]
            traffic = columns[3]
            percent = columns[4]

            data = {'name': name,
                    'url': url,
                    'description': description,
                    'traffic': traffic,
                    'percent': percent}
            write_csv(data)


if __name__ == '__main__':
    main()