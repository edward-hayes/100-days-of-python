import requests
from datetime import datetime, tzinfo
from dateutil import tz
from mailer import Email
import time

MY_LAT = "" # Your latitude
MY_LONG = "" # Your longitude
MY_TIMEZONE = ('America/New_York')

email = Email()

# ------------------ GET CURRENT ISS POSITION ----------------------  #
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()

iss_latitude = float(iss_data["iss_position"]["latitude"])
iss_longitude = float(iss_data["iss_position"]["longitude"])

def iss_is_close():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LONG) < 5:
        return True

# ------------------- CHECK IF IT'S DARK OUTSIDE -------------------   #

sun_parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

sun_response = requests.get("https://api.sunrise-sunset.org/json", params=sun_parameters)
sun_response.raise_for_status()
sun_data = sun_response.json()

sunrise_data = sun_data["results"]["sunrise"].split("+")[0]
sunrise_utc = datetime.strptime(sunrise_data, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=tz.gettz('UTC'))
sunrise = sunrise_utc.astimezone(tz.gettz(MY_TIMEZONE))

sunset_data = sun_data["results"]["sunset"].split("+")[0]
sunset_utc = datetime.strptime(sunset_data, "%Y-%m-%dT%H:%M:%S").replace(tzinfo=tz.gettz('UTC'))
sunset = sunset_utc.astimezone(tz.gettz(MY_TIMEZONE))

time_now = datetime.now().astimezone(tz.gettz(MY_TIMEZONE))

def is_nighttime():
     if sunrise >= time_now or time_now <= sunset:
         return True


while True:
    time.sleep(60)
    if is_nighttime() and iss_is_close():
        subject = "The ISS is Close"
        message = "Look Up👆"
        email.send_msg(to_address=email.email,subject=subject,message=message)

