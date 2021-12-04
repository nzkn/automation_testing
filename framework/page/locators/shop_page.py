from enum import Enum


class ShopPageLocators(str, Enum):
    ORDER_BTN = 'button-link-buy-in-one-click'
    ORDER_POPUP = 'buy-one-click__popup'
    NAME_INPUT = 'Name'
    PHONE_INPUT = 'buy-in-one-click-phone'
