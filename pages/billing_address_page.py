
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


from pages.base_page import BasePage


class BillingAddressPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name = (By.ID, "billing_first_name")
    last_name = (By.ID, "billing_last_name")
    company = (By.ID, "billing_company")
    country = (By.ID, "billing_country")
    address_1 = (By.ID, "billing_address_1")
    city = (By.ID, "billing_city")
    postcode = (By.ID, "billing_postcode")
    phone = (By.ID, "billing_phone")
    email = (By.ID, "billing_email")
    save_button = (By.NAME, "save_address")
    success_message = (By.CSS_SELECTOR, ".woocommerce-message")
    error_messages = (By.CSS_SELECTOR,"ul.woocommerce-error")
    LOGOUT_LINK = (By.LINK_TEXT, "Logout")


    locator_fields = {
        "first_name": first_name,
        "last_name": last_name,
        "company": company,
        "address_1": address_1,
        "city": city,
        "postcode": postcode,
        "phone": phone,
        "email": email
    }

    field_error = lambda self, field_id: (By.ID, f"billing_{field_id}_error")

    def set_field(self, locator, value):
        self.input_text(locator,value)

    def select_country(self, visible_text):
        select_elem = self.wait.until(EC.visibility_of_element_located(self.country))
        Select(select_elem).select_by_visible_text(visible_text)

    def click_save(self):
        #self.driver.find_element(*self.save_button).click()
        self.click_element(self.save_button)
        # return DashboardPage(self.driver)

    def get_success_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.success_message)).text

    def get_field_error(self, field_id):
        locator = self.field_error(field_id)
        try:
            return self.driver.find_element(*locator).text
        except:
            return None

    def is_save_btn_visible(self):
        try:
            return self.driver.find_element(*self.save_button).is_displayed()
        except:
            return False

    def get_all_billing_field_values(self):
        values = {}
        for field_name, locator in self.locator_fields.items():
            try:
                value = self.get_attribute_when_visible(locator, "value")
                values[field_name] = value
            except Exception:
                values[field_name] = None  # or raise if strict checking
        return values

    def get_email_value_on_save_default(self):
        return  self.get_attribute_when_visible(self.email,"value")

    def clear_billing_field_values(self):
        for field_data in self.locator_fields.values():
            field = self.wait.until(EC.presence_of_element_located(field_data))
            field.clear()

    def get_error_messages(self):
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.woocommerce-error")))
        errors = self.driver.find_elements(By.CSS_SELECTOR, "ul.woocommerce-error li")
        #errors = self.finds(self.error_messages)
        return [error.text.strip() for error in errors]

    def click_logout(self):
        self.click_element(self.LOGOUT_LINK)

    def enter_address_details(self,first_name,last_name,company,address_1,city,postcode,phone,email):
        self.input_text(self.first_name, first_name)
        self.input_text(self.last_name, last_name)
        self.input_text(self.company,company)
        # billing_page.select_country(data["country"])
        self.input_text(self.address_1,address_1)
        self.input_text(self.city, city)
        self.input_text(self.postcode,postcode)
        self.input_text(self.phone,phone)
        self.input_text(self.email, email)

