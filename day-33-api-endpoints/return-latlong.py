import json
import requests

API_KEY = ""


parameters = {
    "q": "Raleigh, NC, US",
    "appid": API_KEY
}

response = requests.get(url="http://api.openweathermap.org/geo/1.0/direct",params=parameters)
response.raise_for_status()

data = response.json()
lon = data[0]["lon"]

#print(f"lat is {lat} and long is {lon}")
print(data)
print(lon)