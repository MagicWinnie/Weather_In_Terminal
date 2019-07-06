# -*- coding: utf-8 -*-
import requests
from lxml import etree
import itertools
from bs4 import BeautifulSoup
from lxml import html
from numpy import savetxt
import numpy as np
import pandas as pd
import time
from coolterm import color
import geocoder
f = open("weather.txt","r+")
temp = f.readline()
if temp=="" or time.time()-float(temp)>=3600:
    res = []
    geolocation = False
    if geolocation == True:
        g = geocoder.ip('me')
        city = g.city
        print(city)
    else:
        city = 'Novosibirsk'
    DATAURL = 'https://yandex.ru/pogoda/{0}'.format(city)
    session = requests.session()
    req_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8'
    }
    r = session.get(DATAURL, headers=req_headers, allow_redirects=True)
    html=r.text
    soup = BeautifulSoup(html,features="lxml")
    w_list = soup.find_all('div', class_='fact__temp-wrap')[0]
    humidity_list = soup.find_all('div', class_='fact__props fact__props_position_middle')[0]
    hourly_list = soup.find_all('div', class_='swiper-wrapper')[0]
    # print(w_list,humidity_list,hourly_list)
    first = ""
    first += color.Cyan+color.Bold+"Weather in "+city+":"+color.ResetAll+"\n"
    first += color.Bold+"Temperature: "+color.ResetAll
    temperature = w_list.find_all('span',class_='temp__value')[0].text.strip()
    first += temperature+"°C"+"\n"
    condition = w_list.find_all('div', class_='link__condition day-anchor i-bem')[0].text.strip()
    first += color.Bold+"Condition: "+color.ResetAll+condition+"\n"
    wind = humidity_list.find_all('dd', class_='term__value')[0].text.strip()
    first += color.Bold+"Wind: "+color.ResetAll + wind + "\n"
    humidity = humidity_list.find_all('dl', class_='term term_orient_v fact__humidity')[0].text.strip()
    first += color.Bold+"Humidity: "+color.ResetAll+humidity+"\n"
    pressure = humidity_list.find_all('dl', class_='term term_orient_v fact__pressure')[0].find('dd', class_="term__value").text.strip()
    first += color.Bold+"Pressure: "+color.ResetAll+pressure
    f.truncate(0)
    f.write(str(time.time())+'\n')
    f.write(first)
    print(first)
else:
    print(f.read())

# second = ""
# hhourly = str(hourly_list.text.strip())
# hourly = ""
# for hour in hhourly:
#     if hour.isalpha():
#         break
#     # if hour
#     hourly += hour
# hourly = hourly[:len(hourly)-5]
# hours = []
# temp = []
# for hour in hourly:
#     if hour == "+" or hour == "-":
