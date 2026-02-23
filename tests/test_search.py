from pages.home_page import HomePage
from utils.browser_factory import BrowserFactory


def test_search():
    browser = BrowserFactory(headless=False)
    page = browser.start()
    home_page = HomePage(page)
    home_page.open()
    assert home_page.is_loaded(), "Home page didn't loaded!"

    home_page.fill_location("miami")
    home_page.click_search()
    browser.stop()


test_search()
# if __name__ == "_main_":
#     test_search()
