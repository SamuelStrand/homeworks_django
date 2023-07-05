from django.shortcuts import render

from selenium import webdriver
from bs4 import BeautifulSoup
import requests


def weather(request, mul: str):
    response = requests.get(
        "https://weather.com/weather/monthly/l/5ead5bf0831e9c4adb7cc4a4f0f66264147a55a24823c075c67035cbfb30724b")
    text = response.text
    soup = BeautifulSoup(text, 'html.parser')
    weather_data = []
    day = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempHigh--3k9Yr'}).text
    weather_data.append({'day', day})
    night = int(mul) * soup.find('div', {'class': 'CalendarDateCell--tempLow--2WL7c'}).text
    weather_data.append({'night', night})
    date = int(mul) * soup.find('span', {'class': 'CalendarDateCell--date--JO3Db'}).text
    weather_data.append({'date', date})
    return render(request, 'weather.html', {'day': weather_data})


from selenium.webdriver.chrome.options import Options


def currency(request):
    options = Options()
    options.headless = True
    options.add_argument('--headless')

  
    driver = webdriver.Chrome(options=options)
    driver.get('https://kurs.kz')
    usd_rate = driver.find_element_by_xpath('//div[@id="USD"]/div[@class="value"]')
    eur_rate = driver.find_element_by_xpath('//div[@id="EUR"]/div[@class="value"]')
    usd_text = usd_rate.text
    eur_text = eur_rate.text
    driver.quit()

    context = {'usd_rate': usd_text, 'eur_rate': eur_text}
    return render(request, 'currency.html', context)
