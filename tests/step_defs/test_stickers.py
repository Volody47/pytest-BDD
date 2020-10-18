

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Constants
from selenium.webdriver.support.wait import WebDriverWait

url = "https://litecart.stqa.ru/en/"

# Scenarios
scenarios('../acceptance/acceptance.feature')

# Fixtures

@pytest.fixture
def browser():
    # For this example, we will use Firefox
    # You can change this fixture to use other browsers, too.
    # A better practice would be to get browser choice from a config file.
    b = webdriver.Chrome()
    # b.implicitly_wait(10)
    yield b
    b.quit()

@given("I open url")
def load_url(browser):
    browser.get(url)

# @then("I'm on the home page")
# def step_impl(browser):
#     expected_url = url
#     assert browser.current_url == expected_url

@when(parsers.parse('I looking for "{products}"'))
def search_product(browser, products):
    product_items = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))

    

@when(parsers.parse('I count the "{stickers}"'))
def search_stickers(browser, stickers):
    product_items = WebDriverWait(browser, 5).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product a.link")))
    i = 0
    for sticker in product_items:
        stickers = product_items[i].find_elements(By.CSS_SELECTOR, ".sticker")
        browser.stickers = stickers
        i += 1

@then("each product should have only one sticker")
def step_impl(browser):
    assert len(browser.stickers) == 1, "Should be just one sticker for each item"