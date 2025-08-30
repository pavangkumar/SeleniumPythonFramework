from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

from .dash_board_page import DashboardPage


class RegistrationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    EMAIL = (By.ID, "reg_email")
    PASSWORD = (By.ID, "reg_password")
    REGISTER_BTN = (By.NAME, "register")
    ERROR_MSG = (By.CSS_SELECTOR, "ul.woocommerce-error li")
    WEAK_PWD_ERR_MSG=(By.XPATH,"//div[@class='woocommerce-password-strength short']")


    def open_my_account(self):
        self.click_element(self.MY_ACCOUNT)

    def register_user(self, email, password):
        self.input_text(self.EMAIL, email)
        self.input_password(self.PASSWORD, password)
        self.click_element(self.REGISTER_BTN)
        return DashboardPage(self.driver)

    def register_user_with_weak_pwd(self, email, password):
        self.input_text(self.EMAIL, email)
        self.input_text(self.PASSWORD, password)


    def register_user_with_invalid_email(self,email,pwd):
        self.input_text(self.EMAIL, email)
        self.input_text(self.PASSWORD, pwd)
        time.sleep(3)
        self.click_element(self.REGISTER_BTN)
        return self.get_Js_tooltipfor_invalidmail(self.EMAIL)

    def is_register_btn_enabled(self):
        return self.is_element_visible_enabled(self.REGISTER_BTN)
    def is_email_btn_enabled(self):
        return self.is_element_visible_enabled(self.EMAIL)
    def is_pwd_btn_enabled(self):
        return self.is_element_visible_enabled(self.PASSWORD)

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MSG)

    def get_weak_pwd_error_message(self):
        return self.get_element_text(self.WEAK_PWD_ERR_MSG)

    def is_register_btn_disabled(self):
        return self.get_attribute(self.REGISTER_BTN, "disabled") == "disabled"


