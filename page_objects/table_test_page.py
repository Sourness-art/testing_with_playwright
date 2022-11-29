from playwright.sync_api import Page

from Locators.table_test_page_locators import *


class TableTestPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_table_page(self):
        self.page.locator(BUTTON_TO_TABLE_TEST_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/tag/table.html")

    def get_table_row_amount(self):
        return self.page.locator(TABLE_ROWS).count()

    def get_values(self):
        return self.page.locator(TABLE_DATA).all_inner_texts()