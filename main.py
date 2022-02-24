from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

CHROME_DRIVER_PATH = '/Users/kuba/Development/chromedriver'
ACCOUNT_TO_FOLLOW = 'winerylovers'
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get('PASSWORD')


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.url = 'https://www.instagram.com'

    def login(self):
        self.driver.get(f"{self.url}/accounts/login")
        time.sleep(1)
        username = self.driver.find_element_by_name('username')
        username.send_keys(USERNAME)
        password = self.driver.find_element_by_name('password')
        password.send_keys(PASSWORD)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        time.sleep(5)
        self.driver.get(f'{self.url}/{ACCOUNT_TO_FOLLOW}')
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

    def follow(self):
        for cycle in range(50):
            follow_buttons = self.driver.find_elements_by_css_selector(".L3NKy")
            buttons = 0
            for button in follow_buttons:
                if button.text == "Obserwuj":
                    buttons += 1
                    button.click()
                    time.sleep(1)
                # To not spam so much :)
                if buttons == 10:
                    break
            self.driver.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
bot.driver.quit()
