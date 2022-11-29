from playwright.sync_api import Page

from Locators.basic_triangle_locators import *


class BasicTrianglePage:
    def __init__(self, page: Page):
        self.page = page

    def navigate_to_button_based_triangle_page(self):
        self.page.get_by_role("link", name="The Famous Triangle Application").click()
        self.page.wait_for_url("https://testpages.herokuapp.com/styled/apps/triangle/triangle001.html")

    def enter_data_for_equilateral_triangle(self):
        self.page.get_by_label(SIDE_1).fill("1")
        self.page.get_by_label(SIDE_2).fill("1")
        self.page.get_by_label(SIDE_3).fill("1")

    def enter_data_for_scalene_triangle(self):
        self.page.get_by_label(SIDE_1).fill("3")
        self.page.get_by_label(SIDE_2).fill("4")
        self.page.get_by_label(SIDE_3).fill("5")

    def enter_data_for_isosceles_triangle(self):
        self.page.get_by_label(SIDE_1).fill("3")
        self.page.get_by_label(SIDE_2).fill("4")
        self.page.get_by_label(SIDE_3).fill("3")

    def enter_data_for_not_a_triangle(self):
        self.page.get_by_label(SIDE_1).fill("3")
        self.page.get_by_label(SIDE_2).fill("2")
        self.page.get_by_label(SIDE_3).fill("1")

    def identify_triangle_type(self):
        self.page.locator(IDENTIFY_BUTTON).click()

    def get_triangle_type(self):
        return self.page.locator(TYPE).inner_text()
