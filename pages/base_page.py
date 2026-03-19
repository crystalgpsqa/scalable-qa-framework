#from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_title(self):
        return self.driver.title
    
    def find(self, locator):
        return self.driver.find_element(*locator)