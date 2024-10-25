from selenium import webdriver
from config.config import config


class Client():
    def __init__(self, email: str, password: str) -> None:
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--incognito')
        self.driver = webdriver.Firefox(options=self.options)


    async def start_browser(self):
        self.driver.