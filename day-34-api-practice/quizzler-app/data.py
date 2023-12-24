import requests


URL = "https://opentdb.com/api.php"
CATEGORY = "11" #11 is "Entertainment:Film"; different cats can be found in API docs

class QuizData():
    def __init__(self) -> None:
        self.question_bank = []
        self.parameters ={
            "amount": "10",
            "type": "boolean",
            "category": CATEGORY
        }
        self.get_new_data(self.parameters)

    def get_new_data(self,params):
        response = requests.get(URL, params=params)
        response.raise_for_status()
        data = response.json()
        self.question_bank = data["results"]

