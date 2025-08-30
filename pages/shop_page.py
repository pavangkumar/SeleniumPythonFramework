from selenium.webdriver.common.by import By
from .base_page import BasePage
from .cart_page import CartPage


class ShopPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # ADDRESS_PAGE_VALIDATION=(By.CSS_SELECTOR,".woocommerce-MyAccount-content p")
    # EDIT_BTN =(By.XPATH,"//a[contains(@href,'billing')]")
    # success_message = (By.CSS_SELECTOR, ".woocommerce-message")
    ADDRESS_LOCATOR = (By.XPATH, "//h3[contains(.,'Billing Address')]/following::address[1]")
    VIEW_CART = (By.XPATH, "//a[@title='View your shopping cart']")

    def get_product_add_button(self, product_name):
            """
            Returns the WebElement of 'Add to Cart' button for a given product
            """
            xpath = f"//h3[text()='{product_name}']/following::a[contains(@class,'add_to_cart_button')][1]"
            return self.driver.find_element(By.XPATH, xpath)

    def add_product_to_cart(self, product_name):
            """
            Clicks 'Add to Cart' for a given product
            """
            self.get_product_add_button(product_name).click()

    def go_to_cart_page(self):
            """
            Navigates to the shopping cart
            """
            self.click_element(self.VIEW_CART)
            return CartPage(self.driver)


