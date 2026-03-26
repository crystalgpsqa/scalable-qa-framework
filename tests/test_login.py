import pytest
from flows.login_flow import login_direct, login_from_home
from pages.home_page import HomePage


@pytest.mark.smoke
def test_login_direct(driver):
    sinout_button = login_direct(driver, "sldkzlxl@naver.com", "rlagpal12!")

    home_page = HomePage(driver)
    assert home_page.header.is_logged_in()

@pytest.mark.regression
def test_login_from_home(driver):
    sinout_button = login_from_home(driver, "sldkzlxl@naver.com", "rlagpal12!")
    
    home_page = HomePage(driver)
    assert home_page.header.is_logged_in()