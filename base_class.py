from playwright.sync_api import Playwright

from page_objects.alert_box_page import AlertBoxPage
from page_objects.basic_web_page import BasicWebPageExample
from page_objects.fake_alert_page import FakeAlertPage
from page_objects.table_test_page import TableTestPage
from page_objects.element_attributes_examples_page import ElementAttributesExamples
from page_objects.dynamic_table_test_page import DynamicTableTestPage


class TestBase:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless)
        self.context = self.browser.new_context()
        self.context.tracing.start(screenshots=True, snapshots=True, sources=True)
        self.page = self.context.new_page()
        self.base_url = base_url
        self.page.goto(base_url)
        self.basic_web_page_example = BasicWebPageExample(self.page)
        self.table_test_page = TableTestPage(self.page)
        self.element_attributes_examples = ElementAttributesExamples(self.page)
        self.dynamic_table_test_page = DynamicTableTestPage(self.page)
        self.alert_box_page = AlertBoxPage(self.page)
        self.fake_alert_page = FakeAlertPage(self.page)

    # def goto(self, endpoint: str, use_base_url=True):
    #     if use_base_url:
    #         self.page.goto(self.base_url + endpoint)
    #     else:
    #         self.page.goto(endpoint)

    def close(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
