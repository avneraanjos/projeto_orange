import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self):
        edge_options = Options()
        edge_driver_path = r'C:\Users\emers\PycharmProjects\projeto_orange\edgedriver\msedgedriver.exe'
        self.driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
        self._url_login = "https://opensource-demo.orangehrmlive.com"
        self.driver.get(self._url_login)
        self.driver.implicitly_wait(5)


    def login(self, username: str = 'Admin', passwd: str = 'admin123'):
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(passwd)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
