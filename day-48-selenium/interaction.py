from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_excutable = ChromeDriverManager()
service = Service(chrome_excutable.install())

class Driver(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__(service=service)
        self.get("https://en.wikipedia.org/wiki/Main_Page")


with Driver() as driver:
    ## get number of pages
    # num_pages = driver.find_element(By.CSS_SELECTOR,"#articlecount > a").text
    # print(num_pages)

    ## click a link
    # driver.find_element(By.LINK_TEXT,"Jonas Vingegaard").click()
    # input("press enter when you want to close")

    ## enter info into a search box
    # search = driver.find_element(By.NAME,"search")
    # search.send_keys("python")
    # search.send_keys(Keys.ENTER)

    ## submit form
    # driver.get("http://secure-retreat-92358.herokuapp.com/")
    # first_name = driver.find_element(By.NAME,"fName")
    # last_name = driver.find_element(By.NAME,"lName")
    # email = driver.find_element(By.NAME,"email")

    # first_name.send_keys("Chester")
    # last_name.send_keys("McTester")
    # email.send_keys("chester.mctester@gemail.com")

    # submit = driver.find_element(By.CSS_SELECTOR,"form button")
    # submit.click()

    pass
