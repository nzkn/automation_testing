from framework.page.base import Base
from .locators.main_page import MainPageLocator


class MainPage(Base):
    def select_category(self, category: str):
        self._find_element_by_cls(category).click()

    def select_sub_category(self, subcategory: str):
        self._find_element('//*[@title="'+subcategory+'"]').click()

    def select_product(self, product: str):
        self._find_element('//*[@title="'+product+'"]').click()

    def click_compare(self):
        self._find_element_by_cls(MainPageLocator.COMPARE_BTN.value).click()

    def click_buy(self):
        self._find_element(MainPageLocator.BUY_BTN.value).click()

    def switch_to_shop_window(self):
        window_after = self.driver.window_handles[1]
        self.driver.switch_to.window(window_after)
