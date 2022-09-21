from playwright.sync_api import Playwright


class BasicWebPageExample:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.page.goto(base_url)

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

    def close(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
