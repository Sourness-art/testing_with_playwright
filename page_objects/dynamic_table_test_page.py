from playwright.sync_api import Playwright, Page

from Locators.dynamic_table_locators import *


class DynamicTableTestPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_dynamic_table_page(self):
        self.page.locator(BUTTON_TO_DYNAMIC_TABLE_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

    def open_table_data(self):
        self.page.locator(DYNAMIC_TABLE_DATA_BUTTON).click()

    def get_value_in_table(self):
        return self.page.locator(DYNAMIC_TABLE_DATA).all_inner_texts()

    def get_empty_table(self):
        return self.page.locator(DYNAMIC_EMPTY_TABLE).all_inner_texts()

    def add_value_in_a_row(self, data: str):
        self.page.locator(TEXTAREA_FOR_TABLE).fill(f"{data}")

    def refresh_table(self):
        self.page.locator(REFRESH_TABLE_DATA).click()

    def change_table_name(self):
        self.page.locator(TABLE_CAPTION_NAME).fill("Table")

    def get_table_name(self):
        return self.page.locator(TABLE_NAME).all_inner_texts()

    def change_table_id(self):
        self.page.locator(TABLE_CAPTION_ID).fill("dynamic")

    def get_table_id(self):
        return self.page.locator(TABLE_ID).get_attribute("id")
