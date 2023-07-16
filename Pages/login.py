from selenium.webdriver.common.by import By
from .base import BasePage

class LoginPage(BasePage):
    def __init__(self,driver=None,browser=None,base_url=None):
        super(LoginPage, self).__init__(driver=driver, browser=browser,base_url=base_url)
        self._url_login = self._base_url+"/auth/login"

        #self.driver.get(self._url_login)
        self.driver.implicitly_wait(3)

    def login(self, username: str, passwd: str):
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(passwd)
        self.click_button(By.CSS_SELECTOR, '[type="submit"]')
