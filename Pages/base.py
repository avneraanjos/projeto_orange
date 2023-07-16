from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from typing import Any

class BasePage():

    def __init__(self, driver:Any=None, browser:str=None, base_url:str=None):
        # Initialize WebDriver
        if driver:
            self.driver = driver
        else:
            if browser == 'Chrome':
                self.driver = webdriver.Chrome()
            if browser == 'Edge':
                self.driver = webdriver.Edge()
            if browser == 'Firefox':
                self.driver = webdriver.Firefox()
            else:
                raise ValueError(f' Wrong browser parameter: {browser}.')
        self._base_url= base_url if base_url else ''
        self.driver.implicitly_wait(5)

    def visit(self, base_url='https://opensource-demo.orangehrmlive.com/'):
        return self.driver.get(base_url)

    def wait_element(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((locator)))

    def click_button(self, *locator):
        self.driver.find_element(*locator).click()

