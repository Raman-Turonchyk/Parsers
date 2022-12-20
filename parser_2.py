from bs4 import BeautifulSoup
import requests
import lxml
import json

headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0'
}

# Создаём список ссылок на фестивали
fests_urls_list = []
for i in range(0, 97, 24):
    url = f'https://www.skiddle.com/festivals/search/?ajaxing=1&sort=0&fest_name=&from_date=13%20Aug%202022&to_date=&where%5B%5D=2&where%5B%5D=3&where%5B%5D=4&maxprice=500&o={i}&bannertitle=August'

    req = requests.get(url=url, headers=headers)
    json_data = json.loads(req.text)
    html_response = json_data['html']

    with open(f'data/index_{i}.html', 'w') as file:
        file.write(html_response)

    with open(f'data/index_{i}.html') as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')
    cards = soup.find_all('a', class_='card-details-link')

    for item in cards:
        fest_url = 'https://www.skiddle.com' + item.get('href')
        fests_urls_list.append(fest_url)

# Собираем информацию из наших ссылок
fest_list_result = []
count = 0
for url in fests_urls_list:

    count += 1
    print(count, url, sep='\n')

    req = requests.get(url=url, headers=headers)

    try:
        soup = BeautifulSoup(req.text, 'lxml')

        fest_info_block = soup.find('div', class_='MuiGrid-root MuiGrid-container MuiGrid-spacing-xs-2 css-1ik2gjq')
        fest_name_block = soup.find('div', class_='MuiContainer-root MuiContainer-maxWidthFalse css-1krljt2')
        fest_name = fest_name_block.find('h1').text.strip()
        fest_info = fest_info_block.find_all('span')
        new_fest_info = list(map(lambda x: x.text, fest_info[:4]))
        if 'in' in new_fest_info[-2]:
            fest_location = new_fest_info[-2]
        elif 'in' in new_fest_info[-1]:
            fest_location = new_fest_info[-1]
        else:
            fest_location = 'No location ...'
        if 'From' in new_fest_info[-1]:
            fest_price = new_fest_info[-1]
        elif 'From' in new_fest_info[-2]:
            fest_price = new_fest_info[-2]
        else:
            fest_price = 'No price...'
        fest_date = ', '.join(new_fest_info[:2])

    except Exception as ex:
        print(ex)
        print('Damn...There was some error...')

    fest_list_result.append(
        {
            'Fest name': fest_name,
            'Fest date': fest_date,
            'Fest Location': fest_location,
            'Fest Price': fest_price
        }
    )

with open('fest_list_result.json', 'w', encoding='utf-8') as file:
    json.dump(fest_list_result, file, indent=4, ensure_ascii=False)