from playwright.sync_api import Page


class ElementAttributesExamples:
    def __init__(self, page: Page):
        self.page = page

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

