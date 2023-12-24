import requests

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph520"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_date = "20220519"
update_endpoint = f"{graph_endpoint}/{pixel_date}"

headers = {
    "X-USER-TOKEN": TOKEN
}

parameters = {
    "quantity": "1"
}

response = requests.put(url=update_endpoint, json=parameters, headers=headers)
print(response.text)