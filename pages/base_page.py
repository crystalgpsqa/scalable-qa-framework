from pages.components.modal import Modal
from config.settings import DEFAULT_TIMEOUT, SHORT_TIMEOUT
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    ElementClickInterceptedException,
    StaleElementReferenceException, TimeoutException
)

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DEFAULT_TIMEOUT)
        self.waitS = WebDriverWait(driver, SHORT_TIMEOUT)

    def handle_global_modal(self):
        modal = Modal(self.driver)
        modal.close_if_present()
    
    def find(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))
        #return self.driver.find_element(*locator)
    
    def click(self, locator):
        self.handle_global_modal()
        element = self.wait.until(EC.presence_of_element_located(locator))
        #element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
            #element = self.wait.until(EC.element_to_be_clickable(locator))       
        except(ElementClickInterceptedException, StaleElementReferenceException):
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            self.driver.execute_script("arguments[0].click();", element)
            #self.driver.execute_script("arguments[0].click();", element) v3
            #element = self.wait.until(EC.element_to_be_clickable(locator)) v2
            #element.click() v2
        #self.find(locator).click() v1

    def type(self, locator, text):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.clear()
        element.send_keys(text)

    def get_value(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.get_attribute("value")
    
    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
        #return self.find(locator).text

    def get_title(self):
        return self.driver.title



    def is_present(self, locator):
        short_wait = WebDriverWait(self.driver, SHORT_TIMEOUT)
        try:
            short_wait.until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False
        
    def is_visible(self, locator):
        short_wait = WebDriverWait(self.driver, SHORT_TIMEOUT)
        try:
            element = self.driver.find_element(*locator)
            return self.driver.execute_script("""
                const el = arguments[0];
                const style = window.getComputedStyle(el);
                return style.display !== 'none' &&
                    style.visibility !== 'hidden' &&
                    style.opacity !== '0';
            """, element)
            #short_wait.until(EC.visibility_of_element_located(locator))
            #return True
        except TimeoutException:
            return False