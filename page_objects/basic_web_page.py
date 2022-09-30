from playwright.sync_api import Page

from Locators.basic_web_page_locators import *


class BasicWebPageExample:
    def __init__(self, page: Page):
        self.page = page

    def check_main_page(self):
        assert self.page.locator(MAIN_PAGE_TITLE).is_visible()

    def navigate_to_basic_page(self):
        self.page.locator(BUTTON_TO_BASIC_WEB_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/basic-web-page-test.html")

    def check_basic_page(self):
        assert self.page.locator(BASIC_WEB_PAGE_TITLE).is_visible()
        assert self.page.locator(FIRST_PARAGRAPH).is_visible()
        assert self.page.locator(SECOND_PARAGRAPH).is_visible()

    def return_to_main_page(self):

        self.page.locator(BUTTON_TO_MAIN_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/index.html")
