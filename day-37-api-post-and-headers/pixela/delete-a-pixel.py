import requests

USERNAME = ""
TOKEN = ""
GRAPH_ID = "graph520"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
pixel_date = "20220519"
delete_endpoint = f"{graph_endpoint}/{pixel_date}"

headers = {
    "X-USER-TOKEN": TOKEN
}

response = requests.put(url=delete_endpoint, headers=headers)
print(response.text)