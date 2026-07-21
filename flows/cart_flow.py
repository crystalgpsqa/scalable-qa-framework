from flows.search_flow import search_product
from pages.search_result_page import SearchResultPage


def add_first_search_result_to_cart(driver, keyword):
    search_product(driver, keyword)

    search_result_page = SearchResultPage(driver)
    search_result_page.wait_until_loaded()

    product_detail_page = search_result_page.click_first_product()
    product_detail_page.select_first_option_if_present()
    product_detail_page.click_add_to_cart()
    product_detail_page.wait_until_add_to_cart_popup_visible()

    return product_detail_page