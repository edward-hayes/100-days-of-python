from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_excutable = ChromeDriverManager()
service = Service(chrome_excutable.install())

class Driver(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__(service=service)    
        

with Driver() as driver:
    # gets price from amazon page
    # driver.get("https://www.amazon.com/Widescreen-Anti-Glare-Business-Ultrawide-Computer/dp/B08Q3HR8FB/ref=sr_1_3?crid=1IIV8TYBEUQ6N&keywords=hp+m27f+27%22+full+hd+1920+x+1080+ips+d-sub%2C+hdmi+monitor&qid=1659030036&sprefix=%2Caps%2C186&sr=8-3")
    # price = driver.find_element(By.CLASS_NAME, "a-offscreen")
    # print(price.get_attribute('innerHTML'))

    # driver.get("https://www.python.org/")
    # search_bar = driver.find_element(By.NAME,"q")
    # search_bar.tag_name()
    # print(search_bar)

    # driver.get("https://www.python.org/")
    # documentation_link = driver.find_element(By.CSS_SELECTOR,".documentation-widget a")
    # print(documentation_link.text)

    # driver.get("https://www.python.org/")
    # bug_link = driver.find_element(By.XPATH,'//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
    # print(bug_link.text)

    #input("Press any key to close")
    pass

