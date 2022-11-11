import csv
import requests
from bs4 import BeautifulSoup
from utils import benchmark
from multiprocessing import Pool
from datetime import datetime

def get_html(url):
    responce = requests.get(url)
    return responce.text

def get_deps_links(html):
    urls = []
    soup = BeautifulSoup(html, 'lxml')
    catalog = soup.find('div', class_='grid-deputs')
    deputaty = catalog.find_all('div', class_='dep-item')
    for dep in deputaty:
        a = dep.find('a').get('href')
        link = 'http://kenesh.kg' + a
        urls.append(link)
    return urls

def get_all_links():
    links = []
    for i in range(1,6):
        url = f'http://kenesh.kg/ru/deputy/list/35?page={i}'
        html = get_html(url)
        deps_links = get_deps_links(html)
        links.extend(deps_links)
    return links

def get_page_data(link):
    html = get_html(link)
    soup = BeautifulSoup(html, 'lxml')
    try:
        name = soup.find('div', class_='deput-name').text
    except:
        name = 'Нет имени!'

    container = soup.find('div', class_='ck-editor')
    bio = [tag.text for tag in container.find_all('p')]
    str_bio = ' '.join(bio)
    if len(str_bio.strip()) < 10:
        str_bio = container.find('pre').text

    data = {'name': name, 'bio': str_bio, 'link': link}
    return data

def write_csv(data):
    with open('deputaty.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((data['name'], data['bio'], data['link']))
        print(f'{data["name"]} - parsed!')

def prepare_csv():
    with open('deputaty.csv', 'w') as file:
        writer = csv.writer(file)
        writer.writerow(('ФИО', 'Биография', 'Ссылка на страницу'))

def make_all(link):
    data = get_page_data(link)
    write_csv(data)

@benchmark
def main():
    prepare_csv()
    links = get_all_links()

    # for link in links: # последовательно
    #     data = get_page_data(link)
    #     write_csv(data) 
    start = datetime.now()
    with Pool(20) as pool: # парралельно
        pool.map(make_all, links)
    finish = datetime.now()
    print(f'Парсинг занял: {finish - start}')


if __name__ == '__main__':
    main()
