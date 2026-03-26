from pages.base_page import BasePage
from config.settings import LOGIN_URL
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "goLogin")

    def open(self):
        self.driver.get(LOGIN_URL)

    def enter_username(self, username):
        self.type(self.USERNAME_INPUT, username)

    def enter_password(self, password):
        self.type(self.PASSWORD_INPUT, password)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)