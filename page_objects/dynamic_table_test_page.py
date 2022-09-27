from playwright.sync_api import Playwright, Page


class DynamicTableTestPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_dynamic_table_page(self):
        self.page.locator("text=Dynamic Table Test Page").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/tag/dynamic-table.html")

    def add_value_in_a_row(self):
        self.page.locator("text=Table Data").click()
        self.page.locator("textarea").fill("{\"name\" : \"John\", \"age\" : 22}")
        self.page.locator("text=Refresh Table").click()

    def get_table_row_amount(self):
        return self.page.locator("#mytable > tbody > tr").count()

    def get_value_in_table(self):
        data_table = {"", ""}
        for s in range(self.get_table_row_amount()):
            s += 1
            if s + 1 <= self.get_table_row_amount():
                col1_1 = self.page.locator(
                    f"#dynamictable > tr:nth-child({s + 2}) > td:nth-child(1)").all_inner_texts()
                col2_1 = self.page.locator(
                    f"#mytable > tbody > tr:nth-child({s + 2}) > td:nth-child(2)").all_inner_texts()
                data_table.update(col1_1, col2_1)
        return sorted(data_table)
