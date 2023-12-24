from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

PROMISED_DOWN = 1500
PROMISED_UP = 1000
TWITTER_EMAIL = ""
TWITTER_PASSWORD = "" 

chrome_excutable = ChromeDriverManager()
service = Service(chrome_excutable.install())

class InternetSpeedTwitterBot(webdriver.Chrome):
    def __init__(self) -> None:
        super().__init__(service=service)
        self.implicitly_wait(300)

    def get_internet_speeds(self):
        self.get("https://www.speedtest.net/")
        start_button = self.find_element(By.CSS_SELECTOR,".js-start-test")
        start_button.click()

        wait = WebDriverWait(self,300)
        wait.until(EC.url_contains("result"))

        download_speed = self.find_element(By.CSS_SELECTOR,"span.download-speed").text
        upload_speed = self.find_element(By.CSS_SELECTOR,"span.upload-speed").text

        self.download_speed = float(download_speed)
        self.upload_speed = float(upload_speed)
        self.ref_id = self.current_url

    def tweet_at_provider(self,message: str):
        self.login_to_twitter()
        self.compose_tweet(message)

        send = self.find_element(By.CSS_SELECTOR,"div[role=button][data-testid='tweetButton']")
        send.click()


    def compose_tweet(self,message: str):
        url = "https://twitter.com/compose/tweet"
        self.get(url)
        wait = WebDriverWait(self,10)
        wait.until(EC.url_to_be(url))
        textbox = self.find_element(By.CSS_SELECTOR,"div[role=textbox]")
        textbox.send_keys(message)
        textbox.send_keys(Keys.ENTER)



    def login_to_twitter(self):
        self.get("https://twitter.com/i/flow/login")
        input_email = WebDriverWait(self,10).until(
            EC.presence_of_element_located((By.NAME,"text")))
        input_email.send_keys(TWITTER_EMAIL)
        input_email.send_keys(Keys.ENTER)

        input_password = self.find_element(By.NAME,"password")
        input_password.send_keys(TWITTER_PASSWORD)
        input_password.send_keys(Keys.ENTER)
        
        

with InternetSpeedTwitterBot() as complainer_bot:
    complainer_bot.get_internet_speeds()

    if complainer_bot.download_speed < PROMISED_DOWN or complainer_bot.upload_speed < PROMISED_UP:
        complainer_bot.tweet_at_provider(
            message= ''.join((
                f"Hey Internet Provider, why am I getting {complainer_bot.download_speed}Mbps / {complainer_bot.upload_speed}Mbps?\n",
                f"My promised speeds are {PROMISED_DOWN}Mbps / {PROMISED_UP}Mbps.\n",
                f"Speed Test Results: {complainer_bot.ref_id}"
            ))
            )

    input("press return when complete")

