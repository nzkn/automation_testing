from typing import Type, Final

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from .browser_type import BrowserType


# Реалізувати Factory для роботи в різних браузерах(різні драйвера)
class _DriverFactory:
    __drivers: dict[BrowserType, Type[WebDriver]] = {
        BrowserType.CHROME: webdriver.Chrome(),
        BrowserType.EDGE: webdriver.Edge,
        BrowserType.FIREFOX: webdriver.Firefox,
        BrowserType.INTERNET_EXPLORER: webdriver.Ie,
        BrowserType.OPERA: webdriver.Opera,
        BrowserType.SAFARI: webdriver.Safari
    }
    __driver: Final[WebDriver] = None

    def get_web_driver(self, name: BrowserType) -> WebDriver:
        if not self.__driver:
            self.__driver = self.__drivers[name]()
        return self.__driver


factory = _DriverFactory()

__all__ = ['factory']
