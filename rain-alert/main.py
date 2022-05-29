import requests
import pandas as pd
import json

MY_LAT = "" # Your latitude
MY_LONG = "" # Your longitude

API_KEY = "" # Your API KEY for openweathermap
URL = "https://api.openweathermap.org/data/2.5/onecall"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "units": "imperial",
    "exclude": "current,minutely,daily"
}

response = requests.get(URL,params=parameters)
response.raise_for_status()

weather_data = response.json()
next_12_hours = weather_data["hourly"][:12]
df_weather = pd.json_normalize(next_12_hours, 'weather')
if df_weather['id'].min() < 700:
    print("bring an umbrella")
else:
    print("no umbrella needed")

# next_12_hours = weather_data["hourly"][:12]

# print(next_12_hours)