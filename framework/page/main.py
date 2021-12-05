from framework.page.base import Base
from .locators.main_page import MainPageLocator


class MainPage(Base):
    def select_category(self, category: str, url: str):
        self._find_element_by_cls(category).click()
        assert self.driver.current_url == url

    def select_sub_category(self, subcategory: str, url: str):
        self._find_element_by_xpath('//*[@title="' + subcategory + '"]').click()
        assert self.driver.current_url == url

    def select_product(self, product: str):
        self._find_element_by_xpath('//*[@title="' + product + '"]').click()

    def click_compare(self):
        self._find_element_by_cls(MainPageLocator.COMPARE_BTN.value).click()

    def scroll_to_buy(self):
        self._action_chain.move_to_element(self._find_element_by_cls(MainPageLocator.COMPARE_BTN.value))

    def click_buy(self):
        self._find_element_by_xpath(MainPageLocator.BUY_BTN.value).click()

    def switch_to_shop_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
