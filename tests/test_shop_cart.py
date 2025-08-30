import time

import pytest

from pages.header_saction_page import HeaderPage
from tests.BaseTest import BaseTest
from utilities.read_configurations import ReadConfig
from utilities.json_data_reader import load_json

# Load product list via external JSON reader
products = load_json("products.json")["products"]

class TestShop(BaseTest):
    VALID_USER = ReadConfig.get_username()
    VALID_PASS = ReadConfig.get_password()

    @pytest.mark.regression
    @pytest.mark.parametrize("product", products)
    def test_add_and_delete_product_with_out_login(self, product):
        header_page = HeaderPage(self.driver)
        shop_page=header_page.navigate_to_shop_page()
        # Add product
        shop_page.add_product_to_cart(product)
        cart_page=shop_page.go_to_cart_page()
        assert cart_page.is_product_added_in_cart(product), f"{product} not found in cart"
        # Delete product
        cart_page.delete_product(product)
        time.sleep(5)
        assert not cart_page.is_product_added_in_cart(product), f"{product} still in cart after deletion"
        cart_page.return_to_shop()

    def test_add_multiple_products_and_delete_with_out_login(self):
        header_page = HeaderPage(self.driver)
        shop_page=header_page.navigate_to_shop_page()
        # Add all products from JSON
        for product in products:
            shop_page.add_product_to_cart(product)
        # Navigate to cart
        time.sleep(2)
        cart_page=shop_page.go_to_cart_page()
        # Verify all products are in cart
        for product in products:
            assert cart_page.is_product_added_in_cart(product), f"{product} not found in cart"
        # Delete all products
        for product in products:
            cart_page.delete_product(product)
        # Final validation: cart should be empty)
        assert "Your basket is currently empty." in  cart_page.verify_cart_empty_message()
        cart_page.return_to_shop()


    @pytest.mark.parametrize("product", products)
    def test_add_and_delete_product_with_login(self, product):
            header_page = HeaderPage(self.driver)
            login_page = header_page.navigate_to_login_page()
            dash_board_page = login_page.login(self.VALID_USER, self.VALID_PASS)
            # dash_board_page.is_logout_visible()
            assert dash_board_page.is_logout_visible() is True
            user, domain = self.VALID_USER.split("@")
            assert f"{user}" in dash_board_page.reg_success_user()
            shop_page = header_page.navigate_to_shop_page()
            # Add product
            shop_page.add_product_to_cart(product)
            cart_page = shop_page.go_to_cart_page()
            assert cart_page.is_product_added_in_cart(product), f"{product} not found in cart"
            # Delete product
            cart_page.delete_product(product)
            time.sleep(5)
            assert not cart_page.is_product_added_in_cart(product), f"{product} still in cart after deletion"
            cart_page.return_to_shop()
            header_page.open_my_account()
            dash_board_page.click_logout()

    @pytest.mark.regression
    def test_add_multiple_products_and_delete_with_login(self):
            header_page = HeaderPage(self.driver)
            shop_page = header_page.navigate_to_shop_page()
            # Add all products from JSON
            for product in products:
                shop_page.add_product_to_cart(product)
            # Navigate to cart
            time.sleep(2)
            cart_page = shop_page.go_to_cart_page()
            # Verify all products are in cart
            for product in products:
                assert cart_page.is_product_added_in_cart(product), f"{product} not found in cart"
            # Delete all products
            for product in products:
                cart_page.delete_product(product)
            # Final validation: cart should be empty)
            assert "Your basket is currently empty." in cart_page.verify_cart_empty_message()
            cart_page.return_to_shop()
