import time

from pytest import fixture

from framework.driver.browser_type import BrowserType
from framework.driver.webdriver import Driver
from framework.page.main import MainPage
from framework.page.shop_page import ShopPage


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@fixture(scope='class')
def driver(request):
    webdriver = BrowserType(request.config.option.browser)
    driver = Driver(webdriver)
    driver.get('https://hotline.ua/')
    yield driver
    time.sleep(2)
    driver.quit()


@fixture(scope='class')
def main_page(driver) -> MainPage:
    return MainPage(driver)


@fixture(scope='class')
def shop_page(driver) -> ShopPage:
    return ShopPage(driver)
