import pytest
from pages.home_page import HomePage
from flows.login_flow import login_direct, login_from_home
from tests.test_data.login_data import LOGIN_VALIDATION_FAIL_DATA
from config.settings import USERNAME, PASSWORD

@pytest.mark.smoke
def test_login_direct(driver):
    result = login_direct(driver, USERNAME, PASSWORD)
    
    home_page = HomePage(driver)

    assert home_page.header.is_logged_in()

@pytest.mark.regression
def test_login_from_home(driver):
    result = login_from_home(driver, USERNAME, PASSWORD)

    home_page = HomePage(driver)

    assert home_page.header.is_logged_in()


@pytest.mark.parametrize("data", LOGIN_VALIDATION_FAIL_DATA)
def test_login_validation_fail_cases(driver, data):
    result = login_direct(driver, data["username"], data["password"])

    assert result["success"] is False

    assert result["reason"] == data["reason"]
        