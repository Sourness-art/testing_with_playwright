import time

from playwright.sync_api import Page

from Locators.alert_box_page_locators import *


class AlertBoxPage:

    def __init__(self, page: Page):
        self.page = page

    def navigate_alert_page(self):
        self.page.locator(BUTTON_TO_ALERT_BOX_PAGE).click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/alerts/alert-test.html")

    def usual_alert_box(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        # self.page.on("dialog", lambda dialog: print(dialog.message))
        # time.sleep(1)
        self.page.locator(ALERT_BOX_BUTTON).click()

    def confirm_alert_box(self):
        self.page.once("dialog", lambda dialog: dialog.accept())
        self.page.locator(CONFIRM_BOX_BUTTON).click()

    def get_confirm_result(self):
        return self.page.locator(RESULT_TEXT).all_inner_texts()

    def dismiss_alert_box(self):
        self.page.once("dialog", lambda dialog: dialog.dismiss())
        self.page.locator(CONFIRM_BOX_BUTTON).click()

    def prompt_alert_box(self, prompt_text: str):
        self.page.once("dialog", lambda dialog: dialog.accept(f"{prompt_text}"))
        self.page.locator(PROMPT_BOX_BUTTON).click()

    def get_prompt_text(self):
        return self.page.locator(PROMPT_TEXT).all_inner_texts()
