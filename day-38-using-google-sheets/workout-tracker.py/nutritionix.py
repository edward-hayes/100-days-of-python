import requests

BASE_URL = "https://trackapi.nutritionix.com/"
EXERCISE_ENDPOINT = "/v2/natural/exercise"

class Nutritionix():
    def __init__(self, application_id, api_key, user_stats:dict) -> None:
        self.exercise_url = f"{BASE_URL}{EXERCISE_ENDPOINT}"
        self.header = {
            "x-app-id": application_id,
            "x-app-key": api_key,
            "x-remote-user-id": "1" 
        }
        self.parameters = {
            "query": "",
            "gender": user_stats["gender"],
            "weight_kg": user_stats["weight_kg"],
            "height_cm": user_stats["height_cm"],
            "age": user_stats["age"]
        }
        self.response = {
        }

    def parse_api_response(self, api_response):
        api_response = api_response["exercises"][0]
        self.response["exercise"] = api_response["name"].title()
        self.response["duration"] = api_response["duration_min"]
        self.response["calories"] = api_response["nf_calories"]

    def parse_user_input(self, query):
        self.parameters["query"] = query
        api_response = requests.post(
            url = self.exercise_url,
            headers = self.header,
            json = self.parameters
        )
        print(api_response.json())
        self.parse_api_response(api_response.json())
        
