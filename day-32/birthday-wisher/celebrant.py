import pandas as pd
from datetime import date

class Celebrant():
    def __init__(self, birthdays_csv) -> None:
        self.data = pd.DataFrame()
        self.todays_birthdays = pd.DataFrame()
        self.birthdays_csv = birthdays_csv
        self.create_dataframe()


    def create_dataframe(self):
        self.data = pd.read_csv(self.birthdays_csv)

    def get_todays_birthdays(self):    
        today = date.today()
        self.todays_birthdays = self.data.loc[(self.data['month'] == today.month) & (self.data['day'] == today.day) ] 

