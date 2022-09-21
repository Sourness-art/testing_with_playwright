from playwright.sync_api import sync_playwright
from pytest import fixture

from page_objects.basic_web_page_example import BasicWebPageExample
from page_objects.element_attributes_examples import ElementAttributesExamples
from page_objects.table_test_page import TableTestPage


@fixture
def playwright_init():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def basic_web_page_example(playwright_init):
    app = BasicWebPageExample(playwright_init, base_url="https://testpages.herokuapp.com/styled/index.html")
    yield app
    app.close()


@fixture
def element_attributes_examples(playwright_init):
    app = ElementAttributesExamples(playwright_init, base_url="https://testpages.herokuapp.com/styled/index.html")
    yield app
    app.close()


@fixture
def table_test_page(playwright_init):
    app = TableTestPage(playwright_init, base_url="https://testpages.herokuapp.com/styled/index.html")
    yield app
    app.close()
