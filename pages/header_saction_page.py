from selenium.webdriver.common.by import By
from .base_page import BasePage
from selenium import webdriver


from .login_page import LoginPage
from .registration_page import RegistrationPage
from .shop_page import ShopPage


class HeaderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    SHOP_LINK = (By.LINK_TEXT, "Shop")
    ERROR_MSG = (By.CSS_SELECTOR, "ul.woocommerce-error li")


    def open_my_account(self):
        self.click_element(self.MY_ACCOUNT)

    def open_shop_page(self):
        self.click_element(self.SHOP_LINK)

    def navigate_to_login_page(self):
        self.open_my_account()
        return LoginPage(self.driver)



    def navigate_to_registration_page(self):
        self.open_my_account()
        return RegistrationPage(self.driver)

    def navigate_to_shop_page(self):
        self.open_shop_page()
        return ShopPage(self.driver)


    def get_error_message(self):
        return self.get_element_text(self.ERROR_MSG)

    def check_authenticate_state(self):
        self.driver.get("https://practice.automationtesting.in/my-account/edit-address/")

    def is_login_btn_visible(self):
        try:
            return self.driver.find_element(*self.LOGIN_BTN).is_displayed()
        except:
            return False