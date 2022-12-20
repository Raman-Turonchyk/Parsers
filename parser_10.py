from bs4 import BeautifulSoup
import re


# .find()
# .find_all()
# .parent
# .find_parent()
# .find_next_sibling()
# .find_previous_sibling()


def get_salary(s):
    pattern = r'\d+'
    salary = re.search(pattern, s).group()
    return salary



def get_copywriter(tag):
    whois = tag.find('div', id='whois').text.strip()
    if 'Copywriter' in whois:
        return tag
    return None


def main():
    file = open(r'C:\Users\Vladimir Turonchik\Desktop\Книги Python\[SW.BAND] [Олег Молчанов] Python ООП (2020)\[SW.BAND] Практический курс парсинга сайтов на Python\[SW.BAND] 06 Продвинутые приемы работы с библиотекой BeautifulSoup\исходник\index.html', 'r', encoding='utf8').read()

    soup = BeautifulSoup(file, 'lxml')
    # row = soup.find('div', {'data-set': 'salary'})
    #
    # alena = soup.find('div', text='Alena').find_parent(class_='row')
    # print(alena)

    # copyriters = []
    # persons = soup.find_all('div', class_='row')
    # for person in persons:
    #     item = get_copywriter(person)
    #     if item:
    #         copyriters.append(item)
    #
    # print(copyriters)

    salary = soup.find_all('div', {'data-set': 'salary'})
    for item in salary:
        print(get_salary(item.text.strip()))


if __name__ == '__main__':
    main()