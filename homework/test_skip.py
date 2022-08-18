"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(scope='function')
def browser_desktop():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 1200
    browser.config._window_height = 1100


@pytest.fixture(scope='function')
def browser_mobile():
    browser.config.browser_name = 'chrome'
    browser.config.window_width = 310
    browser.config._window_height = 516


def test_github_desktop(browser_mobile):
    if browser.config.window_width < 1000:
        pytest.skip('Size for mobile version')
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


def test_github_mobile(browser_desktop):
    if browser.config.window_height > 1000:
        pytest.skip('Size for browser version')
    browser.open('https://github.com/')
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
