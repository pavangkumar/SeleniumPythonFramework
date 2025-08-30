from selenium.webdriver.common.by import By
from .base_page import BasePage
from .dash_board_page import DashboardPage
from selenium import webdriver


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    MY_ACCOUNT = (By.LINK_TEXT, "My Account")
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.NAME, "login")
    ERROR_MSG = (By.CSS_SELECTOR, "ul.woocommerce-error li")


    def open_my_account(self):
        self.click_element(self.MY_ACCOUNT)

    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click_element(self.LOGIN_BTN)
        return DashboardPage(self.driver)

    def is_password_masked(self):
        return self.get_attribute(self.PASSWORD, "type") == "password"

    def get_error_message(self):
        return self.get_element_text(self.ERROR_MSG)

    def check_authenticate_state(self):
        self.driver.get("https://practice.automationtesting.in/my-account/edit-address/")

    def is_login_btn_visible(self):
        try:
            return self.driver.find_element(*self.LOGIN_BTN).is_displayed()
        except:
            return False