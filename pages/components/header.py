from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Header(BasePage):
    LOGO = (By.TAG_NAME, "h1")
    SEARCH_INPUT = (By.CSS_SELECTOR, "[data-testid='header-search-box-input']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "[data-testid='header-search-box-input-button']")
    ACCOUNT_BUTTON = (By.CSS_SELECTOR, "[data-testid='header-sign-in-button']")
    ACCOUNT_BUTTON_IS_LOGGED_IN = (By.CSS_SELECTOR, "[data-testid='header-account-button']")
    SIGN_IN_BUTTON = (By.ID, "goLoginBtn")
    SIGN_OUT_BUTTON = (By.CSS_SELECTOR, ".goLogout")

    def search(self, keyword):
        self.type(self.SEARCH_INPUT, keyword)
        self.click(self.SEARCH_BUTTON)


    def wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(self.LOGO))
        #self.wait.until(EC.visibility_of_element_located(self.ACCOUNT_BUTTON))

    #def get_logo(self):
            #return self.find(self.LOGO)
            
    def wait_until_logged_in(self):
        try:
            self.wait.until(
                EC.element_to_be_clickable(self.ACCOUNT_BUTTON_IS_LOGGED_IN)
            )
            return True
        except:
            return False

    def open_account_menu(self):
        self.click(self.ACCOUNT_BUTTON)

    def open_account_menu_if_logged_in(self):
        self.click(self.ACCOUNT_BUTTON_IS_LOGGED_IN)

    def click_sign_in(self):
        self.click(self.SIGN_IN_BUTTON)

    def is_logged_in(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.SIGN_OUT_BUTTON)
            )
            return True
        except:
            return False