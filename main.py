import os
import time
from dotenv import load_dotenv
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

load_dotenv()

SIMILAR_ACCOUNT = "disney"

URL = f"https://www.instagram.com/{SIMILAR_ACCOUNT}/"

class InstaFollower:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.driver.get(URL)
        self.username = os.getenv("INSTA_USERNAME")
        self.password = os.getenv('INSTA_PASSWORD')

    def login(self):

        time.sleep(5)
        login_button = self.driver.find_element(By.XPATH, '//div[contains(text(), "Log in")]')
        login_button.click()

        time.sleep(5)
        username_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[1]/div/label/input')
        username_input.send_keys(self.username)

        password_input = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[2]/div/label/input')
        password_input.send_keys(self.password)

        time.sleep(2)
        login_button = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]')
        print(login_button.text)
        login_button.click()

        time.sleep(20)
        button1 = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Not now')]")
        print(button1.text)
        button1.click()

    def find_followers(self):
        pass

    def follow(self):
        pass

    def reel(self):
        time.sleep(10)
        reel_section = self.driver.find_element(By.XPATH,
                                           '/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[2]/div[4]/span/div/a/div')
        print(reel_section.text)
        reel_section.click()

        while True:
            time.sleep(15)
            element = self.driver.find_element(By.TAG_NAME, 'Body')
            element.click()
            element.send_keys(Keys.PAGE_DOWN)


# chrome_option.add_argument('--start-maximized')

bot = InstaFollower()
bot.login()
# bot.reel()


