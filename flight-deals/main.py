import os
import pandas as pd
from datetime import datetime, timedelta
from dotenv import load_dotenv
from sheets import GoogleSheets
from signal_messenger import Signal
from flight_search import FlightSearch

load_dotenv()
ORIGIN_CITY_CODE = "RDU"
SIGNAL_SERVER_URL = 'http://192.168.86.100:8888/v2/send'
PATH_TO_CREDS_JSON = "my-first-project-350923-2f50a4e12c6d.json"
FLIGHT_SEARCH_API = os.getenv("TEQUILA_API_KEY")


flight_search = FlightSearch(api_key=FLIGHT_SEARCH_API)

data_manager = GoogleSheets(
    path_to_creds_json=PATH_TO_CREDS_JSON,
    spreadsheet_name= "Flight Deals"
)
price_sheet = data_manager.get_sheet("price")

notification_manager = Signal(
    api_url= SIGNAL_SERVER_URL,
    from_number= "+12627079865"
)

def add_iata_codes():
    for index,row in price_sheet.iterrows():
        if not row["IATA Code"]:
            iata_code = flight_search.get_iata_code(city_name=row["City"])
        price_sheet.at[index, "IATA Code"] = iata_code

    data_manager.update_sheet(
        sheet_name="price", 
        dataframe= price_sheet)

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(180))

def check_flights():
    add_iata_codes()
    for index, row in price_sheet.iterrows():
        flight = flight_search.check_flights(
            origin_city_code=ORIGIN_CITY_CODE,
            destination_city_code=row["IATA Code"],
            from_time=tomorrow,
            to_time=six_month_from_today
        )
        if flight is not None and flight['price'] < int(row["Lowest Price"]):
            notification_manager.send_text(
                recipients=["+12627079865"],
                message = ''.join((f"🤑Low Price Alert! You can fly ", 
                    f"from {flight['origin_city']} ({flight['origin_airport']}) ", 
                    f"to {flight['destination_city']} ({flight['destination_airport']}) ", \
                    f"for only ${flight['price']}"
                ))
            )
            notification_manager.send_text(
                recipients=["+12627079865"],
                message = ''.join((
                    f"✈️Flight Details: \n", \
                    f"Departure: Flight {flight['out_flight_airline']} {flight['out_date']} \n",
                    f"Return: Flight {flight['return_flight_airline']} {flight['return_date']} \n",
                ))
            )

check_flights()

