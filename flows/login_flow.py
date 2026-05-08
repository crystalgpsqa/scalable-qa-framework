import time
from pages import login_page
from pages import home_page
from pages.home_page import HomePage
from pages.login_page import LoginPage
from utils.error_parser import parse_error_message


def login_direct(driver, username, password):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    time.sleep(0.1)
    login_page.click_login()
    alert_text = login_page.alert.wait_and_handle_alert()

    if alert_text:
        print("ALERT TEXT:", repr(alert_text))
        reason = parse_error_message(alert_text)

        return {
            "success": False,
            "reason": reason,
            "message": alert_text
        }
    
    if home_page.header.wait_until_logged_in():
        home_page.header.open_account_menu_if_logged_in()
        return {
            "success": True,
            "reason": None,
            "message": None
        }
    
    return {
        "success": False,
        "reason": "unknown_error",
        "message": None
    }



def login_from_home(driver, username, password):
    home_page = HomePage(driver)
    
    home_page.open()
    home_page.header.wait_until_loaded()
    home_page.header.open_account_menu()
    home_page.header.click_sign_in()

    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    home_page.header.wait_until_logged_in()
    home_page.header.open_account_menu_if_logged_in()
    