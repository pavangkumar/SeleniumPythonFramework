import pytest

from pages.header_saction_page import HeaderPage
from pages.login_page import LoginPage
from tests.BaseTest import BaseTest
from utilities.read_configurations import ReadConfig


class TestLogin(BaseTest):
    VALID_USER = ReadConfig.get_username()
    VALID_PASS = ReadConfig.get_password()

    @pytest.mark.regression
    def test_login_with_valid_creds_email(self):

        header_page=HeaderPage(self.driver)
        login_page=header_page.navigate_to_login_page()
        dash_board_page=login_page.login(self.VALID_USER, self.VALID_PASS)
        #dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        user, domain = self.VALID_USER.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        dash_board_page.click_logout()

    def test_login_with_valid_creds_username(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        user, domain = self.VALID_USER.split("@")
        dash_board_page=login_page.login(user, self.VALID_PASS)
        #dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        #user, domain = ReadConfig.get_username().split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        dash_board_page.click_logout()

    def test_login_with_email_case_sensitive(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        dash_board_page=login_page.login(self.VALID_USER.upper(), self.VALID_PASS)
        assert dash_board_page.is_logout_visible() is True
        # user, domain = ReadConfig.get_username().split("@")
        user, domain = self.VALID_USER.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        dash_board_page.click_logout()

    @pytest.mark.regression
    def test_login_with_valid_creds_username_case_sensitive(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        user, domain = self.VALID_USER.split("@")
        dash_board_page=login_page.login(user.upper(), self.VALID_PASS)
        #dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        #user, domain = ReadConfig.get_username().split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        dash_board_page.click_logout()
    ############Negative########################################
    def test_login_with_invalid_credentials(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        login_page.login("wrong@test.com", "WrongPass")
        assert "A user could not be found with this email address." in login_page.get_error_message()

    def test_login_with_valid_username_empty_password(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        login_page.login(self.VALID_USER, "")
        assert "Password is required." in login_page.get_error_message()

    def test_login_with_valid_username_wrong_password(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        login_page.login(self.VALID_USER, "wrong@Pass")
        print(login_page.get_error_message())
        assert f"Error: The password you entered for the username {self.VALID_USER} is incorrect. Lost your password?" in login_page.get_error_message()
        #assert "Username is required." in login_page.get_error_message()

    def test_login_with_empty_username_valid_password(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        login_page.login("", self.VALID_PASS)
        assert "Username is required." in login_page.get_error_message()

    def test_login_with_empty_username_password(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        login_page.login("", "")
        assert "Username is required." in login_page.get_error_message()

    def test_password_is_masked(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        assert login_page.is_password_masked() is True

    def test_authentication_redirect(self):
        login_page = LoginPage(self.driver)
        login_page.check_authenticate_state()
        assert login_page.is_login_btn_visible() is True
