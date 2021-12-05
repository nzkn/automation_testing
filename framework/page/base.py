from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import *

from framework.driver.webdriver import Driver


class Base:
    def __init__(self, driver: Driver):
        self.driver = driver

    @property
    def _wait(self):
        return WebDriverWait(self.driver, 5)

    @staticmethod
    def _selector_from_xpath(xpath: str) -> tuple[By, str]:
        return By.XPATH, xpath

    @property
    def _action_chain(self):
        return ActionChains(self.driver)

    def _find_element_by_xpath(self, xpath: str):
        return self.driver.find_element(By.XPATH, xpath)

    def _find_element_by_id(self, element_id: str):
        return self.driver.find_element(By.ID, element_id)

    def _find_element_by_name(self, element_id: str):
        return self.driver.find_element(By.NAME, element_id)

    def _find_element_by_cls(self, cls: str):
        return self.driver.find_element(By.CLASS_NAME, cls)

    def _find_element_by_url(self, link: str):
        return self.driver.find_element(By.LINK_TEXT, link)

    def _wait_for_element(self, xpath: str, msg='') -> WebElement:
        return self._wait.until(presence_of_element_located(self._selector_from_xpath(xpath)), msg)

    def _wait_for_element_to_be_clickable(self, xpath: str, msg='') -> WebElement:
        return self._wait.until(element_to_be_clickable(self._selector_from_xpath(xpath)), msg)

    def _wait_to_locate_text(self, xpath: str, text: str, msg=''):
        return self._wait.until(text_to_be_present_in_element(self._selector_from_xpath(xpath), text), msg)

    def _wait_to_locate_text_in_value(self, xpath: str, text: str, msg=''):
        return self._wait.until(text_to_be_present_in_element_value((By.XPATH, xpath), text), msg)

    def _validate_input(self, xpath: str, keys: str, message=''):
        element = self._find_element_by_xpath(xpath)
        element.clear()
        element.send_keys(keys)
        self._wait_to_locate_text_in_value(xpath, keys, message)
