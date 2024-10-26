from selenium import webdriver
from config.config import BASE_URL


class Client():
    def __init__(self, email: str, password: str) -> None:
        self.email = email
        self.password = password

        self.options = webdriver.FirefoxOptions()
        self.options.add_argument('--incognito')
        self.driver = webdriver.Firefox(options=self.options)
        
        
    async def start_browser(self) -> None:
        self.driver.get(BASE_URL)
    

    async def auth(self) -> bool:
        '''
        Авторизация пользователя
        '''

        ...


    async def close(self) -> bool:
        self.driver.close()