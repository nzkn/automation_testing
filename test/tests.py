from framework.page.locators.main_page import Category, HouseholdSubcategory, CategoryLink, HouseholdSubcategoryLink
from framework.page.locators.shop_page import ShopPageLocators


class TestOrderProduct:

    def test_open_shop(self, main_page):
        main_page.select_category(Category.HOUSEHOLD.value, CategoryLink.HOUSEHOLD.value)
        main_page.select_sub_category(HouseholdSubcategory.WASHING_MACHINES.value,
                                      HouseholdSubcategoryLink.WASHING_MACHINES.value)
        main_page.select_product('Ціни на Samsung WW90T986CSH/UA')
        main_page.click_compare()
        main_page.scroll_to_buy()
        main_page.click_buy()
        main_page.switch_to_shop_window()

    def test_foxtrot_order_product(self, shop_page):
        shop_page.click_instant_order()
        shop_page.focus_input_and_enter(ShopPageLocators.NAME_INPUT.value, 'Nazar')
        shop_page.focus_input_and_enter(ShopPageLocators.PHONE_INPUT.value, '734500500')
        # do not uncomment following line, an order will be placed
        # shop_page.confirm_order_info()

