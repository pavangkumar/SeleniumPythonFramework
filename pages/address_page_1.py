from selenium.webdriver.common.by import By
from .base_page import BasePage


class AddressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
    # *** Locators - update them if the site's HTML differs ***
    first_name = (By.NAME, "billing_first_name")
    last_name = (By.NAME, "billing_last_name")
    company = (By.NAME, "billing_company")
    address_1 = (By.NAME, "billing_address_1")
    address_2 = (By.NAME, "billing_address_2")
    city = (By.NAME, "billing_city")
    postcode = (By.NAME, "billing_postcode")
    phone = (By.NAME, "billing_phone")
    save_button = (By.NAME, "save_address")  # Replace if different

    # Messages / notifications
    notice = (By.CSS_SELECTOR, ".woocommerce-message")
    field_errors = (By.CSS_SELECTOR, ".woocommerce-NoticeGroup .woocommerce-error li")

    def go_to(self):
        self.logger.info("Opening edit address page")
        self.driver.get("https://practice.automationtesting.in/my-account/edit-address/")

    def fill_address(self, data: dict):
        self.logger.info("Filling address form")
        # For each key in data, try to set value if locator exists
        mapping = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "company": self.company,
            "address_1": self.address_1,
            "address_2": self.address_2,
            "city": self.city,
            "postcode": self.postcode,
            "phone": self.phone,
        }
        for key, locator in mapping.items():
            if key in data:
                self.input_text(*locator, text=data[key])

    def submit(self):
        self.logger.info("Submitting address form")
        self.click_element(*self.save_button)

    def get_success_message(self):
        try:
            return self.get_element_text(*self.notice)
        except Exception:
            self.logger.debug("No success notice found")
            return ""

    def get_error_messages(self):
        errs = []
        elements = self.finds(*self.field_errors)
        for el in elements:
            errs.append(el.text.strip())
        return errs
