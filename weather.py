# -*- coding: utf-8 -*-
import time
import os
import getpass
import platform
import numpy as np
import pandas as pd
import geocoder
# from coolterm import color
from pyowm import OWM

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
