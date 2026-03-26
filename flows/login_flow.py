from pages.home_page import HomePage
from pages.login_page import LoginPage


def login_direct(driver, username, password):
    login_page = LoginPage(driver)
    home_page = HomePage(driver)

    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()

    home_page.header.wait_until_logged_in()
    home_page.header.open_account_menu_if_logged_in()


def login_from_home(driver, username, password):
    home_page = HomePage(driver)

    home_page.open()
    home_page.header.wait_until_loaded()
    #home_page.modal.close_modal_if_present()
    home_page.header.open_account_menu()
    home_page.header.click_sign_in()

    login_page = LoginPage(driver)
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()
    
    home_page.header.wait_until_logged_in()
    home_page.header.open_account_menu_if_logged_in()
    #home_page.modal.close_modal_if_present()