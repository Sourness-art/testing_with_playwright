from playwright.sync_api import Playwright


class ElementAttributesExamples:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.page.goto(base_url)

    def navigate_to_attr_page(self):
        self.page.locator("text=Element Attributes Examples").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/attributes-test.html")

    def get_original_title(self):
        return self.page.locator("text=This paragraph has attributes").get_attribute("original-title")

    def get_title(self):
        return self.page.locator("text=This paragraph has attributes").get_attribute("title")

    def get_custom_attrib(self):
        return self.page.locator("text=This paragraph has attributes").get_attribute("custom-attrib")

    def get_nextid_attr(self):
        return self.page.locator("id=jsattributes").get_attribute("nextid")

    def click_add_attribute_button(self):
        self.page.locator("text=Add Another Attribute").click()

    def close(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
