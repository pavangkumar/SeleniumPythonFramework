
import pytest
import time
# from pages.billing_address_page import BillingAddressPage
from pages.header_saction_page import HeaderPage
from tests.BaseTest import BaseTest
from utilities.err_success_messages import ERROR_SUCCESS_MESSAGES
from data.fake_data import  invalid_billing_data, valid_billing_address_data
import pytest_check as check

from utilities.read_configurations import ReadConfig


class TestBillingAddress(BaseTest):
    VALID_USER = ReadConfig.get_username()
    VALID_PASS = ReadConfig.get_password()

    @pytest.mark.regression
    def test_positive_save_billing_address_new_users(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        email = f"auto{int(time.time())}@test.com"
        print(email)
        dash_board_page = reg_page.register_user(email, "StrongPass@123")
        # dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        user, domain = email.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        address_page=dash_board_page.navigate_to_address_page()
        billing_page=address_page.navigate_to_billing_address_page()
        assert billing_page.is_save_btn_visible() is True
        check.is_in(billing_page.get_email_value_on_save_default(), email)
        data = valid_billing_address_data()
        billing_page.enter_address_details(data["first_name"], data["last_name"], data["company"], data["address_1"],
                                           data["city"], data["postcode"], data["phone"], data["email"])
        billing_page.click_save()
        assert "Address changed successfully." in billing_page.get_success_message()
        # Reload and verify data is saved
        address_page=dash_board_page.navigate_to_address_page()
        billing_page=address_page.navigate_to_billing_address_page()
        check.is_in(billing_page.get_email_value_on_save_default(),  data["email"])
        actual_values = billing_page.get_all_billing_field_values()
        print(actual_values)
        for key, expected in data.items():
            actual = actual_values.get(key)
            assert actual == expected, f"Mismatch for '{key}': expected '{expected}', got '{actual}'"

        billing_page.click_logout()


    def test_field_error_messages_validation_negative(self):
        header_page = HeaderPage(self.driver)
        reg_page = header_page.navigate_to_registration_page()
        email = f"auto{int(time.time())}@test.com"
        print(email)
        dash_board_page = reg_page.register_user(email, "StrongPass@123")
        assert dash_board_page.is_logout_visible() is True
        user, domain = email.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        address_page = dash_board_page.navigate_to_address_page()
        billing_page = address_page.navigate_to_billing_address_page()
        assert billing_page.is_save_btn_visible() is True
        billing_page.clear_billing_field_values()
        billing_page.click_save()
        time.sleep(2)
        actual_errors = billing_page.get_error_messages()
        print(actual_errors)
        print(ERROR_SUCCESS_MESSAGES.items())

        for field, expected_message in ERROR_SUCCESS_MESSAGES.items():
            check.is_in(expected_message, actual_errors, f"Missing expected error for '{field}'")

        billing_page.click_logout()

    def test_positive_save_billing_address_registered_user(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        dash_board_page = login_page.login(self.VALID_USER, self.VALID_PASS)
        # dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        user, domain = self.VALID_USER.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        address_page = dash_board_page.navigate_to_address_page()
        billing_page = address_page.navigate_to_billing_address_page()
        assert billing_page.is_save_btn_visible() is True
        billing_page.clear_billing_field_values()
        data = valid_billing_address_data()
        billing_page.enter_address_details(data["first_name"], data["last_name"], data["company"], data["address_1"],
                                           data["city"], data["postcode"], data["phone"], data["email"])
        billing_page.click_save()
        assert "Address changed successfully." in billing_page.get_success_message()
        # Reload and verify data is saved
        address_page = dash_board_page.navigate_to_address_page()
        billing_page = address_page.navigate_to_billing_address_page()
        check.is_in(billing_page.get_email_value_on_save_default(), data["email"])
        actual_values = billing_page.get_all_billing_field_values()
        print(actual_values)
        for key, expected in data.items():
            actual = actual_values.get(key)
            assert actual == expected, f"Mismatch for '{key}': expected '{expected}', got '{actual}'"

        billing_page.click_logout()

    @pytest.mark.regression
    def test_positive_save_billing_address__in_address_page(self):
        header_page = HeaderPage(self.driver)
        login_page = header_page.navigate_to_login_page()
        dash_board_page = login_page.login(self.VALID_USER, self.VALID_PASS)
        # dash_board_page.is_logout_visible()
        assert dash_board_page.is_logout_visible() is True
        user, domain = self.VALID_USER.split("@")
        assert f"{user}" in dash_board_page.reg_success_user()
        address_page = dash_board_page.navigate_to_address_page()
        billing_page = address_page.navigate_to_billing_address_page()
        assert billing_page.is_save_btn_visible() is True
        billing_page.clear_billing_field_values()
        data = valid_billing_address_data()
        billing_page.enter_address_details(data["first_name"], data["last_name"], data["company"], data["address_1"],
                                           data["city"], data["postcode"], data["phone"], data["email"])
        billing_page.click_save()
        assert "Address changed successfully." in billing_page.get_success_message()
        # Reload and verify data is saved
        address_page = dash_board_page.navigate_to_address_page()
        actual_address=address_page.get_billing_address_lines()

        expected_address_details = [
            data["company"],
            f"{data['first_name']} {data['last_name']}",
            data["address_1"],
            f"{data['city']} - {data['postcode']}",
            "Telangana"
        ]

        for i in range(len(expected_address_details)):
            check.equal(actual_address[i], expected_address_details[i],
                        f"Mismatch at line {i + 1}: expected '{expected_address_details[i]}', got '{actual_address[i]}'")

        billing_page.click_logout()
