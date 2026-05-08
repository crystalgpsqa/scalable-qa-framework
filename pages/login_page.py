from pages.base_page import BasePage
from config.settings import LOGIN_URL
from pages.components.alert import alert
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "email")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "goLogin")

    def __init__(self, driver):
        super().__init__(driver)
        self.alert = alert(driver)



    def open(self):
        self.driver.get(LOGIN_URL)

    def enter_username(self, username):
        el = self.wait.until(EC.visibility_of_element_located(self.USERNAME_INPUT))
        el.clear()
        el.send_keys(username)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, el)

        self.wait.until(
            lambda d: el.get_attribute("value") == username
        )
        #self.driver.execute_script("arguments[0].blur();", el)v2
        #self.type(self.USERNAME_INPUT, username) v1
        
    def enter_password(self, password):
        el = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_INPUT))
        el.clear()
        el.send_keys(password)
        self.driver.execute_script("""
            arguments[0].dispatchEvent(new Event('input', { bubbles: true }));
            arguments[0].dispatchEvent(new Event('change', { bubbles: true }));
        """, el)

        self.wait.until(
            lambda d: el.get_attribute("value") == password
        )
        #self.driver.execute_script("arguments[0].blur();", el) v2
        #self.type(self.PASSWORD_INPUT, password) v1


    def click_login(self):
        element = self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON))
        element.click()
        #self.click(self.LOGIN_BUTTON)


    