class HomePage:
    URL = "https://svburger1.co.il#/HomePage"

    def __init__(self, page):
        self.page = page
        self.title_text = "text=Lets start your way to our best burger"
        self.location_input = "#location-name"
        self.search_button = "text=Search"

    def open(self):
        self.page.goto(self.URL)
        self.page.wait_for_timeout(3000)

    def is_loaded(self):
        return self.page.locator(self.title_text).count () == 1

    def fill_location(self, location: str):
        self.page.locator(self.location_input).fill(location)

    def click_search(self):
        self.page.locator(self.search_button).click()
        self.page.wait_for_timeout(5000)
