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
        # data_table = {"", ""}
        # for s in range(self.get_table_row_amount()):
        #     s += 1
        #     if s + 1 <= self.get_table_row_amount():
        #         col1_1 = self.page.locator(
        #             f"#mytable > tbody > tr:nth-child({s + 1}) > td:nth-child(1)").all_inner_texts()
        #         col2_1 = self.page.locator(
        #             f"#mytable > tbody > tr:nth-child({s + 1}) > td:nth-child(2)").all_inner_texts()
        #         data_table.update(col1_1, col2_1)
        # return sorted(data_table)
