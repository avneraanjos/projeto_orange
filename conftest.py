from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import pytest
import configparser
from Pages.login import LoginPage
from Pages.pim import PIMPage

config = configparser.RawConfigParser()
config.read("./conf.ini")

class ReadConfig:
    @staticmethod
    def get_base_url():
        url = config.get("common info", "baseurl")
        return url

    @staticmethod
    def get_username():
        username = config.get("common info", "username")
        return username

    @staticmethod
    def get_password():
        password = config.get("common info", "password")
        return password

@pytest.fixture()
def fixture():
    """
    Fixture para todos os testes da pagina PIM.
    Passos: Inicia o driver, acessa a pagina de login, executa o login e visita a pagina PIM.
    Retorna o pageObject de PIM. Após a execucao do teste, executa driver.quit como tierDown do teste.
    """
    #edge_options = Options()
    #edge_driver_path = r'C:\Users\emers\PycharmProjects\projeto_orange\edgedriver\msedgedriver.exe'
    #self.driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)

    browser = "Firefox"
    page = LoginPage(browser=browser, base_url=ReadConfig.get_base_url())
    page.visit(page._url_login)
    page.wait_element(By.CSS_SELECTOR, ".oxd-form")
    page.login(ReadConfig.get_username(), ReadConfig.get_password())

    page = PIMPage(driver=page.driver, base_url=page._base_url)
    page.visit(page._url_pim)

    # Returna PIM Pageobject no final do setup
    yield page

    # TearDown
    page.driver.quit()
