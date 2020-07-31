# -*- coding: utf-8 -*-
import time
import os
import getpass
import platform
import numpy as np
import pandas as pd
import geocoder
from coolterm import color
from pyowm import OWM

geolocation = False
city = 'Novosibirsk'

operating_system = platform.system()
file_path = '/home/{}'.format(getpass.getuser()) if operating_system == 'Linux' else 'C:/Users/{}'.format(getpass.getuser())

if 'weather.txt' not in os.listdir(file_path):
	api_inp = input("Input your OpenWeatherMap API (it will ask you only once): ")
	f_api_inp = open("{}/weather.txt".format(file_path), "w", encoding="utf-8")
	f_api_inp.write(api_inp)
	f_api_inp.close()

f = open("{}/weather.txt".format(file_path), "r", encoding="utf-8")
file_content = f.readlines()
f.close()

api = file_content[0]
owm = OWM(api)
mgr = owm.weather_manager()

if geolocation:
	g = geocoder.ip('me')
	city = g.city

observation = mgr.weather_at_place(city)
w = observation.weather

result = ""

result += color.Cyan + color.Bold + "Weather in " + city + ":" + color.ResetAll + "\n"

result += color.Bold + "Status: " + color.ResetAll + w.detailed_status + "\n"

result += color.Bold + "Temperature: " + color.ResetAll + str(w.temperature('celsius')['temp']) + "°C" + "\n"

result += color.Bold + "Feels like: " + color.ResetAll + str(w.temperature('celsius')['feels_like']) + "°C" + "\n"

result += color.Bold + "Clouds: " + color.ResetAll + str(w.clouds) + "%" + "\n"

result += color.Bold + "Visibility distance: " + color.ResetAll + str(w.visibility_distance) + " m" + "\n"

result += color.Bold + "Humidity: " + color.ResetAll + str(w.humidity) + "%" + "\n"

result += color.Bold + "Pressure: " + color.ResetAll + str(w.pressure['press']) + " hPa" + "\n"

result += color.Bold + "Wind speed: " + color.ResetAll + str(w.wind()['speed']) + " m/s" + "\n"

result += color.Bold + "Wind angle: " + color.ResetAll + str(w.wind()['deg']) + "°" + "\n"

print(result)
