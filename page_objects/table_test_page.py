from playwright.sync_api import Playwright


class TableTestPage:

    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.page.goto(base_url)

    def navigate_table_page(self):
        self.page.locator("#tablestest").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/tag/table.html")

    def get_table_row_amount(self):
        return self.page.locator("#mytable > tbody > tr").count()

    def get_table_columns_amount(self):
        return self.page.locator("#mytable > tbody > tr > th").count()

    # def get_table_value(self):
    #     i = 1
    #     table = []
    #     while i <= self.get_table_row_amount():
    #         j = 1
    #         while j <= self.get_table_columns_amount():
    #             table.append(
    #                 self.page.locator(f"#mytable > tbody > tr:nth-child({i}) > th:nth-child({j})").all_inner_texts())
    #             j += 1
    #             if j > 2:
    #                 break
    #         i += 1
    #     return table

    def try_get_values(self):

        data_table = {'id': "", 'name': "", 'amount': ""}
        for s in range(self.get_table_row_amount()):
            if s <= self.get_table_row_amount():
                col1_1 = self.page.locator(f"#mytable > tbody > tr:nth-child({s+1}) > th:nth-child(1)").all_inner_texts()
                col2_1 = self.page.locator(f"#mytable > tbody > tr:nth-child({s+1}) > th:nth-child(2)").all_inner_texts()
                data_table.update()
                print(s)
                s += 1
        return data_table

    def close(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
