from playwright.sync_api import Page

from Locators.element_attribute_examples_locators import *


class ElementAttributesExamples:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_attr_page(self):
        self.page.locator(BUTTON_TO_ELEMENTS_ATTRIBUTE_EXAMPLES).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/attributes-test.html")

    def get_original_title(self):
        return self.page.locator(ORIGINAL_TITLE).get_attribute("original-title")

    def get_title(self):
        return self.page.locator(TITLE).get_attribute("title")

    def get_custom_attrib(self):
        return self.page.locator(CUSTOM_ATTRIBUTE).get_attribute("custom-attrib")

    def get_nextid_attr(self):
        return self.page.locator(NEXT_ID).get_attribute("nextid")

    def click_add_attribute_button(self):
        self.page.locator(ADD_ATTR_BUTTON).click()

