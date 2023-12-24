from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_excutable = ChromeDriverManager()
service = Service(chrome_excutable.install())

class Driver(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__(service=service)
        self.get("https://www.python.org/")
        self.events_dictionary = {}
        self.events_table = self.get_events_table()

    def get_events_table(self):
        return self.find_elements(By.CSS_SELECTOR,"div.event-widget > div > ul.menu > li")
        
    
    def get_current_events(self):
        events_table = self.get_events_table()
        for index, event in enumerate(events_table):
            date = event.find_element(By.CSS_SELECTOR,"time").get_attribute("datetime")
            event_link = event.find_element(By.CSS_SELECTOR,"a")
            self.events_dictionary[index] = {
                "date": date,
                "name": event_link.text
            }

with Driver() as driver:
    driver.get_current_events()
    print(driver.events_dictionary)
