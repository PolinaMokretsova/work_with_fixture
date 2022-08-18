"""
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene.support.shared import browser


@pytest.fixture(params=[(1920, 1080), (1024, 768), (420, 768), (320, 768)])
def browser_size(request):
    return request


@pytest.fixture(scope='function', autouse=True)
def browser_config(browser_size):
    browser.open('https://github.com/')
    width = browser_size.param[0]
    height = browser_size.param[1]
    browser.driver.set_window_size(width=width, height=height)


def test_github_desktop(browser_size):
    if browser.driver.get_window_size()["width"] < 1010:
        pytest.skip('Size for mobile version')
    browser.open('https://github.com/')
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


def test_github_mobile():
    if browser.driver.get_window_size()["width"] > 1011:
        pytest.skip('Size for desktop version')
    browser.open('https://github.com/')
    browser.element('[class="octicon octicon-three-bars"]').click()
    browser.element('[class="HeaderMenu-link flex-shrink-0 no-underline"]').click()


