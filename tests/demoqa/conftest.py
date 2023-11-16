import pytest
from selene import browser
import allure

@allure.title('Open start page')
@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    browser.config.window_width = 1530
    browser.config.window_height = 900
    browser.config.base_url = 'https://demoqa.com'

    yield

    browser.quit()
