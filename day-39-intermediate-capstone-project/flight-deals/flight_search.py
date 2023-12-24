import requests
from flight_data import FlightData

BASE_URL = "https://tequila-api.kiwi.com"

class FlightSearch:
    def __init__(self, api_key) -> None:
        self.api_key = api_key
        self.header = {
            "apikey": self.api_key
        }

    def get_iata_code(self,city_name: str) -> str:
        endpoint = "/locations/query"
        locations_api = f"{BASE_URL}{endpoint}"
        parameters = {
            "term" : city_name,
            "location_types": "city"
        }
        response = requests.get(url=locations_api,headers=self.header,params=parameters)
        data = response.json()
        iata_code = data["locations"][0]["code"]
        return iata_code

    def check_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        endpoint = "/v2/search"
        query_api = f"{BASE_URL}{endpoint}"
        parameters = {
            "fly_from": origin_city_code,
            "fly_to": destination_city_code,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=query_api,headers=self.header,params=parameters)
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None

        flight_data = {
            "price" : data["price"],
            "origin_city": data["route"][0]["cityFrom"],
            "origin_airport": data["route"][0]["flyFrom"],
            "destination_city": data["route"][0]["cityTo"],
            "destination_airport": data["route"][0]["flyTo"],
            "out_date" : data["route"][0]["local_departure"].split("T")[0],
            "out_flight_airline": f"{data['route'][0]['airline']}-{data['route'][0]['flight_no']}",
            "return_flight_airline": f"{data['route'][1]['airline']}-{data['route'][1]['flight_no']}",
            "return_date": data["route"][1]["local_departure"].split("T")[0]
        }
        print(f"{flight_data['destination_city']}: ${flight_data['price']}")
        return flight_data
        

