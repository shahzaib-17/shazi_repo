import pytest

# @pytest.mark.usefixtures("driver_fix", "data", "browsers")
from selenium.webdriver.common.by import By

from BaseClass import BaseClass
from Page_Objects.Homepage import Homepage
from seleniume2e.Page_Objects.checkoutpage import checkoutpage


class TestLocators(BaseClass):

    def test_login_locators(self):

        home = Homepage(self.driver)
        self.wait(Homepage.shop)
        home.shop_item().click()

        item = checkoutpage(self.driver)

        cart = item.item_selection()
        names = item.card_header()
        # print(name.text)
        print(len(cart))
        i = -1
        for value in names:
            product = value.text
            i = i + 1
            print(product)
            if product == 'Blackberry':
                cart[i].click()
                break

        item.checkout_button().click()
        print('shazi')