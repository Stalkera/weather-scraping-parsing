import requests
import csv
from bs4 import BeautifulSoup
from time import sleep
import random

f = open('weather.csv', 'w', encoding='utf-8_sig', newline='\n')
f_obj = csv.writer(f)
f_obj.writerow(['ქალაქი', 'კვირის დღე', 'თარიღი', 'დღის ტემპერატურა', 'ღამის ტემპერატურა'])
i = 0
k = 0
city = ['თბილისი', 'რუსთავი', 'ქუთაისი', 'ბათუმი', 'გორი']
while k <= 5 and i <= 5:
    url = f'https://amindi.ge/ka/city/{city[i]}/?d=5'
    r = requests.get(url)
    c = r.text
    soup = BeautifulSoup(c, 'html.parser')
    days = soup.find('div', class_='row px-3')
    all_days = days.find_all('div', class_='col px-0')

    for day in all_days:
        day_name = day.find('div', class_='weekDay').text
        date = day.find('p', class_='day').text
        degree = day.find_all('span')
        degree_value = [item.text for item in degree]
        degree_day = degree_value[0]
        degree_night = degree_value[1]
        f_obj.writerow([city[i], day_name, date, degree_day, degree_night])
    i += 1
    k += 1
    sleep(random.randint(15, 20))
