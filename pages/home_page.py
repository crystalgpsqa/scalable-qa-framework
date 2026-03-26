from pages.base_page import BasePage
from config.settings import BASE_URL
from pages.components.modal import Modal
from pages.components.header import Header
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.modal = Modal(driver)
        self.header = Header(driver)
            

    def open(self):
        self.driver.get(BASE_URL)
    
    


