import time

from selenium import webdriver
from selenium.webdriver.edge.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By



class PMIPage():

    def __init__(self):
        edge_options = Options()
        edge_driver_path = r'C:\Users\emers\PycharmProjects\projeto_orange\edgedriver\msedgedriver.exe'
        self.driver = webdriver.Edge(executable_path=edge_driver_path, options=edge_options)
        self._url_login = "https://opensource-demo.orangehrmlive.com"
        self.driver.get(self._url_login)
        self.driver.implicitly_wait(5)


    def open_PMI(self, username: str = 'Admin', passwd: str = 'admin123'):
        self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(passwd)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
        self.driver.implicitly_wait(1)

    def add(self, name, middle, last):
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button').click()
        self.driver.find_element(By.CSS_SELECTOR, '[name="firstName"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="middleName"]').send_keys(middle)
        self.driver.find_element(By.CSS_SELECTOR, '[name="lastName"]').send_keys(last)
        self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()

    def search(self, text):
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button/i').click()
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(text)
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]').click()

    def validate_search(self, expected_result):
        self.driver.implicitly_wait(5)
        elemento = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]')
        texto_obtido = elemento.text
        palavras_esperadas = expected_result.split()
        if any(palavra in texto_obtido for palavra in palavras_esperadas):
            print("Pelo menos uma palavra esperada está presente no texto obtido.")
        else:
            print(f"Nenhuma das palavras esperadas: {', '.join(palavras_esperadas)}, foi encontrada no texto obtido.")


    def filter_employment_status(self, status):
        wait = WebDriverWait(10)
        element = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')))
        element.click()
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[7]')
        dropdown_element = self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
        dropdown = Select(dropdown_element)
        dropdown.select_by_visible_text(status)
        time.sleep(10)