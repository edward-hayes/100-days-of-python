from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

class Upgrade():
    def __init__(self,id,rate) -> None:
        self.id = id
        self.rate = rate
        self.price = 0

    def set_current_value(self):
        self.value = self.rate / self.price

chrome_excutable = ChromeDriverManager()
service = Service(chrome_excutable.install())

class Driver(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__(service=service)

        self.get("http://orteil.dashnet.org/experiments/cookie/")
        self.cookie = self.find_element(By.ID,"cookie")

    def click_cookie(self,times):
        for _ in range(times):
            self.cookie.click()

    def get_number_of_cookies(self):
        number_of_cookies = self.find_element(By.ID,"money")
        return int(number_of_cookies.text.replace(",",""))

    def get_upgrade_div(self, id):
        return self.find_element(By.CSS_SELECTOR,f"#{id}".replace(' ','\ '))

    def get_current_price(self, id):
        upgrade_div = self.get_upgrade_div(id)
        upgrade_text = upgrade_div.find_element(By.CSS_SELECTOR,"b").text
        price = upgrade_text.split(" - ")[1].replace(",","")
        return int(price)

    def get_upgrade_amount(self,id):
        upgrade_div = self.get_upgrade_div(id)
        try:
            upgrade_amount = upgrade_div.find_element(By.CSS_SELECTOR,"div.amount").text
            return int(upgrade_amount)
        except:
            return 0
        return int(upgrade_amount)


    def buy_upgrade(self,id):
        upgrade_div = self.get_upgrade_div(id)
        upgrade_div.click()

class CookieClicker():
    def __init__(self, upgrade: set[Upgrade],driver: Driver, upgrade_ids: list[str]) -> None:
        self.upgrade = upgrade
        self.driver = driver
        self.upgrade_ids = upgrade_ids
    
    def update_values(self):
        for id in self.upgrade_ids:
            self.upgrade[id].price = self.driver.get_current_price(self.upgrade[id].id)
            self.upgrade[id].set_current_value()

    def get_best_value(self):
        current_values = [self.upgrade[id].value for id in self.upgrade_ids]
        return upgrade_ids[current_values.index(max(current_values))]

    def buy_best_value(self):
        id_of_best_value = self.get_best_value()
        print(f"The best value is {id_of_best_value}")
        price_of_best_value = upgrade[id_of_best_value].price
        num_of_current_cookies = self.driver.get_number_of_cookies()
        if num_of_current_cookies >= price_of_best_value:
            self.driver.buy_upgrade(id_of_best_value)
            self.update_grandma_rate()

    def update_grandma_rate(self):
        count = 0
        for id in self.upgrade_ids:
            upgrade_amount = self.driver.get_upgrade_amount(id)
            if upgrade_amount > 0:
                count = count + 1
        if count > 2 and count < 9:
            self.upgrade['buyGrandma'].rate = .2*(count+2)

upgrade_ids = ['buyCursor','buyGrandma','buyFactory','buyMine','buyShipment','buyAlchemy lab','buyPortal','buyTime machine']
upgrade_rates = [.2,.8,4,10,20,100,1332,24691.2]


with Driver() as driver:
    
    upgrade = {id: Upgrade(id=id,rate=rate) for id,rate in zip(upgrade_ids,upgrade_rates)}
    
    cookie_clicker = CookieClicker(
        upgrade = upgrade,
        driver = driver,
        upgrade_ids = upgrade_ids
    )

    def run(minutes):
        timeout = time.time() + 60 * minutes
        while time.time() < timeout:
            driver.click_cookie(100)
            cookie_clicker.update_values()
            cookie_clicker.buy_best_value()

    run(minutes=5)
    input("5 minutes up! Hit 'return' when done")

