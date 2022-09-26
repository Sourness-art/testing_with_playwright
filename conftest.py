from playwright.sync_api import sync_playwright
from pytest import fixture

from t_base import TestBase


@fixture
def playwright_init():
    with sync_playwright() as playwright:
        yield playwright

@fixture
def t_base(playwright_init):
    t_base = TestBase(playwright_init, base_url='https://testpages.herokuapp.com/styled')
    t_base.goto('/')
    yield t_base
    t_base.close()

#
# @fixture
# def basic_web_page_example(playwright_init):
#     app = BasicWebPageExample(playwright_init)
#     yield app
#     app.close()


# @fixture
# def element_attributes_examples(t_base):
#     # app = ElementAttributesExamples(test_base)
#     app = t_base
#     app.goto('/styled/attributes-test')
#     yield app

#
# @fixture
# def table_test_page(test_base):
#     test_base.goto('/tag/table')
#     yield test_base
#
#
# @fixture
# def dynamic_table_test_page(playwright_init):
#     app = DynamicTableTestPage(playwright_init)
#     yield app
#     app.close()
