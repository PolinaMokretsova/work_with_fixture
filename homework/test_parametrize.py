"""
Переопределите параметр с помощью indirect
"""
import pytest
from selene.support.shared import browser

chrome = pytest.fixture(params=[(1000, 900), (1500, 1200), (900, 500)])


@chrome
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    width = browser_size.param[0]
    height = browser_size.param[1]

    browser.config.window_width = width
    browser.config.window_height = height


@pytest.mark.parametrize("browser_size", [(1100, 1200)], indirect=True)
def test_github_desktop(browser_size):
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


@pytest.mark.parametrize("browser_size", [(414, 896)], indirect=True)
def test_github_mobile(browser_size):
    browser.open('https://github.com/')
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()
