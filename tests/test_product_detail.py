import pytest

from flows.search_flow import search_product
from pages.search_result_page import SearchResultPage
from flows.cart_flow import add_first_search_result_to_cart


@pytest.mark.smoke
def test_open_first_product(driver):
    search_product(driver, "toner")

    search_result_page = SearchResultPage(driver)
    search_result_page.wait_until_loaded()
    product_detail_page = search_result_page.click_first_product()

    assert "/product/detail" in driver.current_url
    assert product_detail_page.get_product_name()
    assert product_detail_page.get_product_brand()
    assert product_detail_page.get_product_price()
    assert product_detail_page.is_product_image_visible()
    assert product_detail_page.is_add_to_cart_button_visible()


@pytest.mark.smoke
def test_select_first_product_option(driver):
    search_product(driver, "toner")

    search_result_page = SearchResultPage(driver)
    search_result_page.wait_until_loaded()

    product_detail_page = search_result_page.click_first_product()

    option_selected = product_detail_page.select_first_option_if_present()

    if not option_selected:
        pytest.skip("첫 번째 상품에 선택 가능한 옵션이 없습니다.")

    selected_option_text = product_detail_page.get_selected_option_text()

    print(f"SELECTED OPTION: {selected_option_text}")

    assert selected_option_text
    assert "Select a Type" not in selected_option_text
    #추후 옵션 상품과 단일 상품 테스트 분리 필요. 세트 상품 케이스는 구조 완성 후 마지막에 추가 예정


@pytest.mark.smoke
def test_increase_product_quantity(driver):
    search_product(driver, "toner")

    search_result_page = SearchResultPage(driver)
    search_result_page.wait_until_loaded()

    product_detail_page = search_result_page.click_first_product()

    product_detail_page.select_first_option_if_present()

    initial_quantity = product_detail_page.get_quantity()
    product_detail_page.increase_quantity()
    increased_quantity = product_detail_page.get_quantity()

    print(f"INITIAL QUANTITY: {initial_quantity}")
    print(f"INCREASED QUANTITY: {increased_quantity}")

    assert initial_quantity == 1
    assert increased_quantity == initial_quantity + 1


@pytest.mark.smoke
def test_add_product_to_cart(driver):
    product_detail_page = add_first_search_result_to_cart(
        driver,
        "toner"
    )

    assert product_detail_page.is_add_to_cart_popup_visible() is True

    product_detail_page.click_view_cart()

    assert "/cart" in driver.current_url