import requests

def guess(name):

    params = {
        "name": name
    }
    age_url = "https://api.agify.io/"
    gender_url = "https://api.genderize.io"

    age_response = requests.get(url=age_url,params=params)
    age = age_response.json()['age']

    gender_response = requests.get(url=gender_url,params=params)
    gender = gender_response.json()['gender']

guess("edward")