from framework.page.base import Base
from framework.page.locators.shop_page import ShopPageLocators


class ShopPage(Base):

    def click_instant_order(self):
        self._find_element_by_id(ShopPageLocators.ORDER_BTN.value).click()

    def focus_input_and_enter(self, name: str, keys: str):
        popup = self._find_element_by_id(ShopPageLocators.ORDER_POPUP.value)
        popup.find_element_by_id(name).send_keys(keys)
