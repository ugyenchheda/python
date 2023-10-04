import requests
 
print("\t\tWelcome to the Weather Forecaster!\n\n")
print("Just Enter the City you want the weather report for and click on the button! It's that simple!\n\n")
 
city_name = input("Enter the name of the City : ")
print("\n\n")
 

def Gen_report(C):
    url = 'https://wttr.in/{}'.format(C)
    try:
        data = requests.get(url)
        T = data.text
    except:
        T = "Error Occurred"
    print(T)
     
Gen_report(city_name)


#alternate option
import requests
import tkinter as tk
import re
from decouple import config

OPEN_WEATHER_MAP_API_KEY = config("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

IPBASE_API_KEY = config("IPBASE_API_KEY")
IPBASE_API_ENDPOINT = "https://api.ipbase.com/v2/info"

IP_ADDRESS_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def get_weather():
    input_value = input_field.get()

    if IP_ADDRESS_REGEX.match(input_value):
        ipbase_query_params = {
            "apiKey": IPBASE_API_KEY,
            "ip": input_value
        }
        response = requests.get(IPBASE_API_ENDPOINT,
                                params=ipbase_query_params)
        city_name = response.json()["data"]["location"]["city"]["name"]

        weather_query_params = {
            'q': city_name,
            'appid': OPEN_WEATHER_MAP_API_KEY,
            'units': 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()

    else:
        # Try to get weather data directly using city name
        weather_query_params = {
            'q': input_value,
            'appid': OPEN_WEATHER_MAP_API_KEY,
            'units': 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()

    # Display weather data
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']}°C")
