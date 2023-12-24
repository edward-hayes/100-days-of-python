import requests

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": "",
    "username": "",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)

#{"message":"Success. Let's visit https://pixe.la/@curiosior , it is your profile page!","isSuccess":true}
#