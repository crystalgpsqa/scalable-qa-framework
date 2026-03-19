from config.settings import BASE_URL
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    LOGO = (By.TAG_NAME, "h1")

    def open(self):
        self.driver.get(BASE_URL)

    def get_logo(self):
        return self.find(self.LOGO)


