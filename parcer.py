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
class color:
    ResetAll = "\033[0m"
    Bold       = "\033[1m"
    Dim        = "\033[2m"
    Underlined = "\033[4m"
    Blink      = "\033[5m"
    Reverse    = "\033[7m"
    Hidden     = "\033[8m"
    ResetBold       = "\033[21m"
    ResetDim        = "\033[22m"
    ResetUnderlined = "\033[24m"
    ResetBlink      = "\033[25m"
    ResetReverse    = "\033[27m"
    ResetHidden     = "\033[28m"
    Default      = "\033[39m"
    Black        = "\033[30m"
    Red          = "\033[31m"
    Green        = "\033[32m"
    Yellow       = "\033[33m"
    Blue         = "\033[34m"
    Magenta      = "\033[35m"
    Cyan         = "\033[36m"
    LightGray    = "\033[37m"
    DarkGray     = "\033[90m"
    LightRed     = "\033[91m"
    LightGreen   = "\033[92m"
    LightYellow  = "\033[93m"
    LightBlue    = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan    = "\033[96m"
    White        = "\033[97m"
    BackgroundDefault      = "\033[49m"
    BackgroundBlack        = "\033[40m"
    BackgroundRed          = "\033[41m"
    BackgroundGreen        = "\033[42m"
    BackgroundYellow       = "\033[43m"
    BackgroundBlue         = "\033[44m"
    BackgroundMagenta      = "\033[45m"
    BackgroundCyan         = "\033[46m"
    BackgroundLightGray    = "\033[47m"
    BackgroundDarkGray     = "\033[100m"
    BackgroundLightRed     = "\033[101m"
    BackgroundLightGreen   = "\033[102m"
    BackgroundLightYellow  = "\033[103m"
    BackgroundLightBlue    = "\033[104m"
    BackgroundLightMagenta = "\033[105m"
    BackgroundLightCyan    = "\033[106m"
    BackgroundWhite        = "\033[107m"
res = []
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
first += color.Cyan+color.Bold+"Weather in "+city+":"+color.ResetAll
first += color.Bold+"\nTemperature: "+color.ResetAll
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
print(first)
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
