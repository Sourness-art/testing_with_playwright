from playwright.sync_api import sync_playwright, Playwright
from pytest import fixture

from base_class import TestBase


@fixture
def playwright_init():
    with sync_playwright() as playwright:
        yield playwright


@fixture
def base_class(playwright_init):
    base_class = TestBase(playwright_init, base_url='https://testpages.herokuapp.com')
    yield base_class
    base_class.close()


@fixture
def gh_context(playwright: Playwright):
    request_context = playwright.request.new_context(base_url="https://rickandmortyapi.com/api/")
    yield request_context
    request_context.dispose()
