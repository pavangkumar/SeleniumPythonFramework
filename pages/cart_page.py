import time

from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    RETURN_TO_SHOP = (By.XPATH, "//p[@class='return-to-shop']/a")
    CART_EMPTY =(By.XPATH,"//p[@class='cart-empty']")

    def is_product_added_in_cart(self, product_name):
        try:
            self.driver.find_element(By.XPATH, f"//td[@class='product-name']/a[contains(text(),'{product_name}')]")
            return True
        except:
            return False

    def delete_product(self, product_name):
        time.sleep(2)
        delete_btn = self.driver.find_element(By.XPATH, f"//td[@class='product-name']/a[contains(text(),'{product_name}')]/ancestor::tr/td/a[@class='remove']")
        delete_btn.click()
        time.sleep(2)

    # def return_to_shop(self):
    #     self.click_element(self.RETURN_TO_SHOP)
    #     return ShopPage(self.driver)

    def verify_cart_empty_message(self):
        return self.get_element_text(self.CART_EMPTY)

    def return_to_shop(self):
         self.click_element(self.RETURN_TO_SHOP)


