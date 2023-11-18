import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function', autouse=True)
def browser_window_config():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1024
    browser.config.window_height = 768
    yield
    browser.quit()