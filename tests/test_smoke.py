import pytest
from pages.home_page import HomePage

@pytest.mark.smoke
def test_smoke(driver):
    home = HomePage(driver)
    home.open()
    assert "OLIVE YOUNG" in home.get_title()

def test_for_fail_screenshot(driver):
    home = HomePage(driver)
    home.open()
    assert False