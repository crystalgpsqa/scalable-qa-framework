from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from pages.product_detail_page import ProductDetailPage


class SearchResultPage(BasePage):
    RESULT_COUNT = (By.CSS_SELECTOR, "span.mr-1.font-bold")
    PRODUCT_CARDS = (By.CSS_SELECTOR, "a[href*='/product/detail']")
    PRODUCT_BRAND = (By.CSS_SELECTOR, "div.truncate")
    PRODUCT_NAME = (By.CSS_SELECTOR, "span.line-clamp-2 span")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "strong.text-coral-50")


    def wait_until_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_CARDS)
        )

    def get_result_count(self):
        self.wait_until_loaded()
        count_text = self.get_text(self.RESULT_COUNT)
        return int(count_text.replace(",", ""))

    def has_results(self):
        return self.get_result_count() > 0
    
    def get_product_count(self):
        return len(self.driver.find_elements(*self.PRODUCT_CARDS))
    
    def get_first_product(self):
        self.wait_until_loaded()

        products = self.driver.find_elements(*self.PRODUCT_CARDS)

        return products[0]
    
    def get_first_product_name(self):
        self.wait_until_loaded()

        first_product = self.driver.find_elements(*self.PRODUCT_NAME)[0]
        return first_product.text
    
    def get_first_product_price(self):
        self.wait_until_loaded()

        return self.driver.find_element(
            *self.PRODUCT_PRICE
        ).text
    
    def click_first_product(self):
        self.click(self.PRODUCT_CARDS)

        product_detail_page = ProductDetailPage(self.driver)
        product_detail_page.wait_until_loaded()

        return product_detail_page
