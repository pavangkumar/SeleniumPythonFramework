import pytest
import time

from pages.header_saction_page import HeaderPage
from tests.BaseTest import BaseTest
import pytest_check as check

#@pytest.mark.usefixtures("setup")
class TestRegistration(BaseTest):

    def test_register_input_fields_enabled(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        check.is_true(reg_page.is_email_btn_enabled())
        check.is_true(reg_page.is_pwd_btn_enabled())
        check.is_true(reg_page.is_register_btn_enabled())

    @pytest.mark.regression
    def test_register_new_user_positive(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        email = f"auto{int(time.time())}@test.com"
        print(email)
        dash_board_page=reg_page.register_user(email, "StrongPass@123")
        #dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        user, domain = email.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        dash_board_page.click_logout()


    def test_invalid_email_format_registration(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        validation_message=reg_page.register_user_with_invalid_email("invalid","StrongPass@123")
        print(validation_message)
        assert "@" in validation_message or "include an '@'" in validation_message, \
            f"Unexpected validation message: {validation_message}"

    @pytest.mark.regression
    def test_missing_period_email_registration(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        validation_message=reg_page.register_user_with_invalid_email("test@domain#com","StrongPass@123")
        print(validation_message)
        assert "A part following '@' should not contain the symbol" in validation_message, \
            f"Unexpected validation message: {validation_message}"

    def test_registration_empty_email(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        reg_page.register_user("", "StrongPass@123")
        assert "Please provide a valid email address." in reg_page.get_error_message()

    def test_registration_empty_password(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        email = f"auto{int(time.time())}@test.com"
        reg_page.register_user(email, "")
        assert "Please enter an account password." in reg_page.get_error_message()

    def test_registration_empty_email_password(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        reg_page.register_user("", "")
        assert "Please provide a valid email address." in reg_page.get_error_message()

    @pytest.mark.regression
    def test_registration_with_weak_password(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        email = f"auto{int(time.time())}@test.com"
        reg_page.register_user_with_weak_pwd(email, "1234")
        check.is_in("Please enter a stronger password.",reg_page.get_weak_pwd_error_message())
        time.sleep(3)
        check.is_false(reg_page.is_register_btn_enabled())
