import requests

SHEETY_BASE_URL = "https://api.sheety.co"

class Sheety():
    def __init__(self, access_id, api_key, proj_endpoint) -> None:
        self.url = f"{SHEETY_BASE_URL}/{access_id}{proj_endpoint}"
        self.header = {
            "Authorization" : f"Bearer {api_key}"
        }

    def post_row(self, sheet, parameters: dict):
        response = requests.post(
            url = f"{self.url}/{sheet}",
            headers=self.header,
            json={
                f"{sheet}": parameters
            }
        )
        #for debugging print(response.json())