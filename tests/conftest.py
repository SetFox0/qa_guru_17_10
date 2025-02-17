import pytest
from selene import browser


@pytest.fixture(scope='session', autouse=True)
def open_browser():
    browser.config.base_url = "https://github.com"
    browser.config.window_width = 1280
    browser.config.window_height = 920

    yield

    browser.quit()