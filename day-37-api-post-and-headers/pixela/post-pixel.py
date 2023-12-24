import requests
from datetime import date


USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph520"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

headers = {
    "X-USER-TOKEN": TOKEN
}

today = date.today()
yyyyddmm = today.strftime("%Y%m%d")

parameters = {
    "date": str(yyyyddmm),
    "quantity": "1"
}

response = requests.post(url=graph_endpoint, json=parameters, headers=headers)
print(response.text)