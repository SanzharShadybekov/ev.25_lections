from bs4 import BeautifulSoup
from decorators import benchmark
import requests
import datetime
import csv

count = 0

def get_html(url: str) -> str:
    '''
    Получает html код определенного сайта
    '''
    response = requests.get(url)
    return response.text

def get_data(html: str) -> bool:
    '''
    Функция парсер, получает все данные с сайта
    '''
    soup = BeautifulSoup(html, 'lxml')
    catalog = soup.find('div', class_='catalog-list')
    if not catalog:
        return False
    cars = catalog.find_all('a', class_='catalog-list-item')
    for car in cars:
        title = car.find('span', class_='catalog-item-caption').text.strip()

        mileage = car.find('span', class_='catalog-item-mileage').text
        if not mileage:
            mileage = 'Нет пробега!'

        price = car.find('span', class_='catalog-item-price').text

        try:
            image = car.find('img', class_='catalog-item-cover-img').get('src')
        except:
            image = 'Нет картинки!'

        data =  {
            'title': title,
            'mileage': mileage,
            'price': price,
            'img': image
        }
        write_to_csv(data)
    return True

def write_to_csv(data: dict) -> None:
    '''функция для записи данных в csv файл'''
    global count
    with open('cars.csv', 'a') as file:
        fieldnames = ['№', 'Марка', 'Пробег', 'Цена', 'Фото']
        writer = csv.DictWriter(file, fieldnames)
        count += 1
        writer.writerow({
            '№': count,
            'Марка': data.get('title'),
            'Пробег': data.get('mileage'),
            'Цена': data.get('price'),
            'Фото': data.get('img')
        })

def prepare_csv() -> None:
    '''Подготавлвает csv файл'''
    with open('cars.csv', 'w') as file:
        fieldnames = ['№', 'Марка', 'Пробег', 'Цена', 'Фото']
        writer = csv.DictWriter(file, fieldnames)
        writer.writerow({
            '№': '№',
            'Марка': 'Марка', 
            'Пробег': 'Пробег',
            'Цена': 'Цена',
            'Фото': 'Фото'
        })

@benchmark
def main():
    i = 1    
    prepare_csv()
    while True:
        BASE_URL = f'https://cars.kg/offers/{i}'
        html = get_html(BASE_URL)
        is_res = get_data(html)
        if not is_res:
            break
        print(f'Cтраница: {i}')
        i += 1
        
main()
