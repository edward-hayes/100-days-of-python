import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

PATH_TO_JSON = "my-first-project-350923-2f50a4e12c6d.json"

class GoogleSheets():
    def __init__(self, path_to_creds_json, spreadsheet_name:str) -> None:
        self.setup(spreadsheet_name, path_to_creds_json)

    def setup(self, spreadhseet_name, creds_path):
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
        client = gspread.authorize(creds)
        self.spreadsheet = client.open(spreadhseet_name)
        

    def get_sheet(self, sheet_name:str):
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet_df = pd.DataFrame(sheet.get_all_values())
        new_header = sheet_df.iloc[0] 
        sheet_df = sheet_df[1:] 
        sheet_df.columns = new_header 
        return sheet_df

    def post_data(self):
        pass

    def update_sheet(self, sheet_name, dataframe: pd.DataFrame):
        sheet = self.spreadsheet.worksheet(sheet_name)
        sheet.update([dataframe.columns.values.tolist()] + dataframe.values.tolist())
