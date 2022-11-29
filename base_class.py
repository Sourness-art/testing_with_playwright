from playwright.sync_api import Playwright

from page_objects.alert_box_page import AlertBoxPage
from page_objects.basic_web_page import BasicWebPageExample
from page_objects.fake_alert_page import FakeAlertPage
from page_objects.table_test_page import TableTestPage
from page_objects.element_attributes_examples_page import ElementAttributesExamples
from page_objects.dynamic_table_test_page import DynamicTableTestPage
from page_objects.growing_button_page import GrowingButtonPage
from page_objects.file_downloading_uploading import FileDownloadingUploading
from page_objects.basic_triangle import BasicTrianglePage


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
        self.growing_button_page = GrowingButtonPage(self.page)
        self.file_downloading_uploading = FileDownloadingUploading(self.page)
        self.basic_triangle_page = BasicTrianglePage(self.page)

    def close(self):
        self.context.tracing.stop(path="trace.zip")
        self.context.close()
        self.browser.close()
