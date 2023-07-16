import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from .base import BasePage
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from typing import Any

class PIMPage(BasePage):

    def __init__(self,driver,base_url=None):
        super(PIMPage, self).__init__(driver=driver,base_url=base_url)
        #url internas
        self._url_pim= self._base_url+'/pim/viewEmployeeList'
        self._url_pim_add_user= self._base_url+'/pim/addEmployee'

        #xpaths da pagina
        self._search_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]'
        self._employee_name_input_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input'
        self._employee_id_input_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input'
        self._table_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div'
        self._reset_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]'
        self._save_btn_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]'
        self._add_user_id_input_xpath = '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input'
        self._delete_btn_xpath = '//*[@id="app"]/div[3]/div/div/div/div[3]/button[2]'

    # def open_PIM(self, username: str = 'Admin', passwd: str = 'admin123'):
    #     self.driver.find_element(By.CSS_SELECTOR, '[name="username"]').send_keys(username)
    #     self.driver.find_element(By.CSS_SELECTOR, '[name="password"]').send_keys(passwd)
    #     self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
    #     self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a/span').click()
    #     self.driver.implicitly_wait(1)

    'input[control-id="ControlID-1"]'

    def add(self, name, middle, last, id):
        self.driver.find_element(By.CSS_SELECTOR, '[name="firstName"]').send_keys(name)
        self.driver.find_element(By.CSS_SELECTOR, '[name="middleName"]').send_keys(middle)
        self.driver.find_element(By.CSS_SELECTOR, '[name="lastName"]').send_keys(last)
        self.driver.find_element(By.XPATH, self._add_user_id_input_xpath).send_keys(Keys.CONTROL + "a")
        self.driver.find_element(By.XPATH, self._add_user_id_input_xpath).send_keys(Keys.DELETE)
        self.driver.find_element(By.XPATH, self._add_user_id_input_xpath).send_keys(id)
        # try:
        #     self.driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
        # except:

    def search(self, text):
        #info div
        toogle_button=self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button/i')
        if toogle_button.get_attribute('class') == 'oxd-icon bi-caret-down-fill':
            self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button/i').click() #toogle information button
        else:
            pass
        #fill the input field
        self.driver.find_element(By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[1]/div/div[2]/div/div/input').send_keys(text)
        #click button search
        self.driver.find_element(By.XPATH, self._search_btn_xpath).click()


    def validate_search(self, expected_result)->bool:
        self.driver.implicitly_wait(5)
        elemento = self.driver.find_element(By.XPATH,'/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div/div/div/div/div[2]/div[2]/div/div[2]')
        texto_obtido = elemento.text
        palavras_esperadas = expected_result.split()
        if any(palavra in texto_obtido for palavra in palavras_esperadas):
            print("Pelo menos uma palavra esperada está presente no texto obtido.")
            return True
        else:
            print(f"Nenhuma das palavras esperadas: {', '.join(palavras_esperadas)}, foi encontrada no texto obtido.")
            return False


    def filter_employment_status(self, status):
        dropdown = self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]')
        time.sleep(2)
        dropdown.click()
        while(dropdown.text) != status:
            print(dropdown.text)
            dropdown.send_keys(Keys.DOWN)
        dropdown.send_keys(Keys.ENTER)
        time.sleep(1)


    def employee_name(self,name:str)->None:
        self.driver.find_element(By.XPATH, self._employee_name_input_xpath).send_keys(name)

    def employee_id(self,id:str)->None:
        self.driver.find_element(By.XPATH, self._employee_id_input_xpath).send_keys(id)

    def click_search_button(self):
        self.click_button(By.XPATH,self._search_btn_xpath)

    def click_reset_button(self):
        self.click_button(By.XPATH,self._reset_btn_xpath)

    def click_save_button(self):
        self.click_button(By.XPATH,self._save_btn_xpath)

    def get_table_data(self)->Any:
        element =  self.driver.find_elements(By.XPATH, self._table_xpath+'[1]/div/div')
        id = element[1].text
        name = element[2].text
        last_name = element[3].text
        contract = element[5].text
        return id,name,last_name,contract

    def delete_employee(self):
        element =  self.driver.find_element(By.XPATH, self._table_xpath+'[1]/div/div[9]/div/button[1]')
        element.click()
        self.driver.find_element(By.XPATH,self._delete_btn_xpath).click()

    def table_size(self)->int:
        return len(self.driver.find_elements(By.XPATH, self._table_xpath))

    def get_table_user_id(self):
        lista = []
        for n in range(1, self.table_size()):
            last_name = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div['+ str(n) +']/div/div[2]').text
            lista.append(last_name)
        return lista

    def order_list_by_id(self):
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[2]/div/i').click()
        self.driver.find_element(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[1]/div/div[2]/div/div/ul/li[1]').click()
        time.sleep(1)