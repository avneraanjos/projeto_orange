from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from Pages.PageObject import PageObject


class LoginPage(PageObject):
    _url_login: str = "https://opensource-demo.orangehrmlive.com"
    #"ControlID-4"

    def __init__(self, browser):
        super(LoginPage, self).__init__(browser=browser)
        self.driver.get(self._url_login)
    def click_login_btn(self):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    def login(self, username:str='Admin', passwd:str='admin123'):
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input').send_keys(passwd)
        self.click_login_btn()
