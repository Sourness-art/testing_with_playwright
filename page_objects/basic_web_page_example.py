from playwright.sync_api import Page


class BasicWebPageExample:
    def __init__(self, page: Page):
        self.page = page

    def check_main_page(self):
        assert self.page.locator("text=Test Pages For Automating").is_visible()
        assert self.page.locator(
            "text=This is a set of pages for automating or testing. Some of the examples are suita").is_visible()

    def check_basic_page(self):
        self.page.locator("text=Basic Web Page Example").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/basic-web-page-test.html")

        assert self.page.locator("text=Basic Web Page Example").is_visible()
        assert self.page.locator("text=A paragraph of text").is_visible()
        assert self.page.locator("text=Another paragraph of text").is_visible()

    def return_to_main_page(self):
        self.page.locator("text=Basic Web Page Example").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/basic-web-page-test.html")

        self.page.locator("text=Index").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/index.html")
