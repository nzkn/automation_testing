from selenium.webdriver.remote.webdriver import WebDriver
from framework.driver.browser_type import BrowserType
from framework.driver.driver_factory import factory
from framework.singleton import Singleton
from selenium import webdriver


# Реалізувати Singleton для веб драйвера
class Driver(WebDriver):
    __metaclass__ = Singleton

    def __init__(self, browser_type: BrowserType):
        driver = webdriver.Chrome()
        # driver = factory.get_web_driver(browser_type)
        driver.implicitly_wait(1)
        driver.set_window_size(1920, 1080)
        self.driver = driver

    def __getattr__(self, item):
        return getattr(self.driver, item)
