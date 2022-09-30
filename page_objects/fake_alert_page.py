from playwright.sync_api import Playwright, sync_playwright, expect, Page

from Locators.fake_alert_locators import *


class FakeAlertPage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_fake_alert_page(self):
        self.page.locator(BUTTON_TO_FAKE_ALERT_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/alerts/fake-alert-test.html")

    def open_fake_alert_box(self):
        self.page.locator(ALERT_BOX_BUTTON).click()

    def check_alert_box_is_visible(self):
        return self.page.locator(ALERT_BOX).is_visible()

    def accept_fake_alert(self):
        self.page.locator(ACCEPT_BUTTON).click()

    def open_modal_box(self):
        self.page.locator(MODAL_BOX_BUTTON).click()

    def accept_modal_box(self):
        self.page.locator(ACCEPT_BUTTON).click()

    def exit_modal_box(self):
        self.page.locator("//div[@class = 'faded-background active']").click()
