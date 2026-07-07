import pytest

from flows.search_flow import search_product
from pages.search_result_page import SearchResultPage


@pytest.mark.smoke
def test_search_product(driver):
    result = search_product(driver, "toner")

    search_result_page = SearchResultPage(driver)
    search_result_page.wait_until_loaded()

    result_count = search_result_page.get_result_count()
    product_count = search_result_page.get_product_count()
    first_product_name = search_result_page.get_first_product_name()
    first_product_price = search_result_page.get_first_product_price()

    print("=" * 50)
    print(f"SEARCH KEYWORD      : {result['keyword']}")
    print(f"SEARCH RESULT COUNT : {result_count}")
    print(f"PRODUCT CARD COUNT  : {product_count}")
    print(f"FIRST PRODUCT       : {first_product_name}")
    print(f"FIRST PRODUCT PRICE : {first_product_price}")
    print("=" * 50)

    assert result["keyword"] == "toner"
    assert "/search/results" in driver.current_url
    assert "query=toner" in driver.current_url
    assert search_result_page.has_results()
    assert product_count > 0
    #assert "toner" in first_product_name.lower()