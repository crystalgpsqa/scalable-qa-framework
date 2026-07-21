from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ProductDetailPage(BasePage):

    PRODUCT_BRAND = (By.CSS_SELECTOR, "[data-testid='product-brand-name']")
    PRODUCT_NAME = (By.CSS_SELECTOR, "[data-testid='product-name']")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "[data-testid='product-price']")
    PRODUCT_IMAGE = (By.CSS_SELECTOR, "[data-testid='product-image']")

    PRODUCT_OPTION_BUTTON = (By.CSS_SELECTOR, "[data-testid='product-option-button']")
    PRODUCT_OPTION_ITEMS = (By.CSS_SELECTOR, "[data-testid='product-option-list'] a.item")

    PRODUCT_QUANTITY_PLUS = (By.CSS_SELECTOR, "[data-testid='product-quantity-plus']")
    PRODUCT_QUANTITY_VALUE = (By.CSS_SELECTOR, "[data-testid='product-quantity-value']")

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "[data-testid='product-addtocart-button']")

    # 페이지 확장 시추후 공통 컴포넌트로 이동 할 것
    VIEW_CART_BUTTON = (By.CSS_SELECTOR, "[data-testid='view-cart-button']")
    CONTINUE_SHOPPING_BUTTON = (By.CSS_SELECTOR, "[data-testid='continue-shopping-button']")

    def wait_until_loaded(self):
        self.wait.until(
            EC.visibility_of_element_located(self.PRODUCT_NAME)
        )

    def get_product_name(self):
        return self.get_text(self.PRODUCT_NAME)

    def get_product_brand(self):
        return self.get_text(self.PRODUCT_BRAND)

    def get_product_price(self):
        return self.get_text(self.PRODUCT_PRICE)
    
    def is_product_image_visible(self):
        return self.is_visible(self.PRODUCT_IMAGE)
    
    def is_add_to_cart_button_visible(self):
        return self.is_visible(self.ADD_TO_CART_BUTTON)
    
    def select_first_option_if_present(self):
        if not self.is_present(self.PRODUCT_OPTION_BUTTON):
            print("[PRODUCT] OPTION BUTTON NOT FOUND")
            return False

        self.click(self.PRODUCT_OPTION_BUTTON)

        option_items = self.wait.until(
            EC.presence_of_all_elements_located(self.PRODUCT_OPTION_ITEMS)
        )

        option_items[0].click()

        print("[PRODUCT] FIRST OPTION SELECTED")
        return True
    
    def get_selected_option_text(self):
        return self.get_text(self.PRODUCT_OPTION_BUTTON)
    
    def increase_quantity(self):
        self.click(self.PRODUCT_QUANTITY_PLUS)
    
    def get_quantity(self):
        return self.get_text(self.PRODUCT_QUANTITY_VALUE)
    
    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BUTTON)

    def is_add_to_cart_popup_visible(self):
        return (
            self.is_present(self.VIEW_CART_BUTTON)
            and self.is_present(self.CONTINUE_SHOPPING_BUTTON)
        )
    
    def click_view_cart(self):
        self.click(self.VIEW_CART_BUTTON) 

    def wait_until_add_to_cart_popup_visible(self):
        self.wait.until(
            EC.visibility_of_element_located(self.VIEW_CART_BUTTON)
        )
        self.wait.until(
            EC.visibility_of_element_located(self.CONTINUE_SHOPPING_BUTTON)
        )