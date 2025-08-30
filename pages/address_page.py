from selenium.webdriver.common.by import By
from .base_page import BasePage
from .billing_address_page import BillingAddressPage


class AddressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    ADDRESS_PAGE_VALIDATION=(By.CSS_SELECTOR,".woocommerce-MyAccount-content p")
    EDIT_BTN =(By.XPATH,"//a[contains(@href,'billing')]")
    success_message = (By.CSS_SELECTOR, ".woocommerce-message")
    ADDRESS_LOCATOR = (By.XPATH, "//h3[contains(.,'Billing Address')]/following::address[1]")

    def get_billing_address_lines(self):
        address_el = self.driver.find_element(*self.ADDRESS_LOCATOR)
        raw_lines = address_el.text.split("\n")
        lines = []
        for line in raw_lines:
            clean_line = line.strip()
            if clean_line:
                lines.append(clean_line)
        return lines

    def validate_address_page(self):
        try:
            return self.get_element_text(*self.ADDRESS_PAGE_VALIDATION)
        except Exception:
            self.logger.debug("No success page found")
            return ""

    def navigate_to_billing_address_page(self):
        self.click_element(self.EDIT_BTN)
        return BillingAddressPage(self.driver)

    def get_weak_pwd_error_message(self):
        return self.get_element_text(self.success_message)

