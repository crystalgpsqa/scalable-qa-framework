from pages.home_page import HomePage


def search_product(driver, keyword):
    home_page = HomePage(driver)
    home_page.open()

    home_page.header.search(keyword)

    return {
        "keyword": keyword
    }