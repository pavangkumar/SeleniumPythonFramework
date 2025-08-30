from selenium.webdriver.common.by import By

from .address_page import AddressPage
from .base_page import BasePage



class DashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    REG_SUCCESS_MSG = (By.XPATH, "//div[contains(@class,'MyAccount-content')]/p/strong")
    LOGOUT_LINK = (By.LINK_TEXT, "Sign out")
    ADDRESS_LINK = (By.LINK_TEXT, "Addresses")
    success_message = (By.CSS_SELECTOR, ".woocommerce-message")

    def open_my_account(self):
        self.click_element(self.MY_ACCOUNT)

    def reg_success_user(self):
        return self.get_element_text(self.REG_SUCCESS_MSG)

    def is_logout_visible(self):
        try:
            return self.driver.find_element(*self.LOGOUT_LINK).is_displayed()
        except:
            return False

    def click_logout(self):
        self.click_element(self.LOGOUT_LINK)

    def navigate_to_address_page(self):
        self.click_element(self.ADDRESS_LINK)
        return AddressPage(self.driver)

    def get_success_message(self):
     return self.get_element_text(self.success_message)

