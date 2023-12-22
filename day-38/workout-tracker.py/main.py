from nutritionix import Nutritionix
from sheety import Sheety
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PROJ_ENDPOINT = "/workoutTracker"

USER_STATS = {
    "gender": "male",
    "weight_kg": "104",
    "height_cm": "180",
    "age": "33"
}

nutritionix = Nutritionix(
    application_id= os.getenv("NUT_APPLICATION_ID"),
    api_key = os.getenv("NUT_API_KEY"),
    user_stats= USER_STATS
)

sheety = Sheety(
    access_id=os.getenv("SHEETY_APP_ID"),
    api_key=os.getenv("SHEETY_API_TOKEN"),
    proj_endpoint=SHEETY_PROJ_ENDPOINT
)

def rows(parameters:dict):
    parameters["date"] = datetime.now().strftime("%m/%d/%Y")
    parameters["time"] = datetime.now().strftime("%X")
    return parameters

def main():
    user_input = input("Tell me what you did: ").lower()
    nutritionix.parse_user_input(user_input)
    sheety.post_row(sheet="workout", parameters=rows(nutritionix.response))

main()