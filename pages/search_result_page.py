from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class SearchResultPage(BasePage):
    RESULT_COUNT = (By.ID, "hitsFound")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "li.prdt-unit")
    PRODUCT_NAMES = (By.CSS_SELECTOR, "li.prdt-unit input[name='prdtName']")

    def get_result_count(self):
        count_text = self.get_text(self.RESULT_COUNT)
        return int(count_text.replace(",", ""))

    def has_results(self):
        return self.get_result_count() > 0
    
    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))
    
    def get_first_product_name(self):
        first_product = self.driver.find_elements(*self.PRODUCT_NAMES)[0]
        return first_product.get_attribute("value")