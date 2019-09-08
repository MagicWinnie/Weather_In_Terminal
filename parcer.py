# -*- coding: utf-8 -*-
import time
import os
import itertools
from coolterm import color

import numpy as np
from numpy import savetxt
import pandas as pd

import requests
from bs4 import BeautifulSoup
from lxml import html
from lxml import etree

import geocoder

if "weather.txt" in os.listdir("/home/dmitrii/"):
	f = open("weather.txt","r+", encoding="utf-8")
else:
	f = open("weather.txt","w", encoding="utf-8")
	f.close()
	f = open("weather.txt","r+", encoding="utf-8")

f.truncate(0)

temp = f.readline()
geolocation = False

if geolocation == True:
	g = geocoder.ip('me')
	city = g.city
	print(city)
else:
	city = 'Novosibirsk'
DATAURL = 'https://yandex.com/pogoda/{0}'.format(city)

res = []
first = ""
session = requests.session()
req_headers = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'ru,en-US;q=0.9,en;q=0.8'
}

if temp=="" or time.time()-float(temp)>=3600:
	r = session.get(DATAURL, headers=req_headers, allow_redirects=True)
	html=r.text
	soup = BeautifulSoup(html,features="lxml")

	w_list = soup.find_all('div', class_='fact__temp-wrap')[0]
	humidity_list = soup.find_all('div', class_='fact__props fact__props_position_middle')[0]
	hourly_list = soup.find_all('div', class_='swiper-wrapper')[0]
	
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