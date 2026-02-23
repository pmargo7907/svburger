from playwright.sync_api import sync_playwright


def launch_browser(playwright):
    browser = playwright.chromium.launch(
        channel="chrome",
        headless=False
    )
    page = browser.new_page()
    return browser, page


def open_home_page(page):
    page.goto("https://svburger1.co.il/#/HomePage")
    page.wait_for_timeout(3000)


def validate_home_page(page):
    title_locator = page.locator("text=Lets start your way to our best burger")
    if title_locator.count() == 1:
        print("✔ Home page loaded successfully")
        return True
    else:
        print("✖ Home page did not load")
        return False


def fill_location_input(page):
    location_input = page.locator("#location-name")
    location_input.click()
    location_input.fill("los angeles")


def click_search_button(page):
    search_button = page.locator("text=Search")
    search_button.click()
    page.wait_for_timeout(5000)


def test_search_in_website():
    with sync_playwright() as playwright:
        browser, page = launch_browser(playwright)

        open_home_page(page)

        if validate_home_page(page):
            fill_location_input(page)
            click_search_button(page)

        browser.close()


test_search_in_website()