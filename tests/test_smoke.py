import pytest
from pages.home_page import HomePage

@pytest.mark.smoke

def test_smoke(driver):
    home = HomePage(driver)
    home.open()
    assert "OLIVE YOUNG" in home.get_title()

    logo = home.get_logo()
    assert logo is not None