from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from utilities.logger import get_logger
import time
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.logger = get_logger(self.__class__.__name__)


    def find(self,locator):
            self.logger.debug(f"Finding element: {locator}")
            return self.driver.find_element( locator)

    def finds(self,locator):
            self.logger.debug(f"Finding elements:{locator}")
            return self.driver.find_elements(locator)

    def wait_for_visible(self, locator):
        try:
            self.logger.debug(f"Waiting for visible: {locator}")
            return self.wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            self.logger.exception(f"Element not visible:{locator}")
            raise

    def wait_for_clickable(self,locator):
        try:
            self.logger.debug(f"Waiting for clickable:{locator}")

            return self.wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.exception(f"Element not clickable: {locator}")
            raise

    def click_element(self,locator):
        self.logger.debug(f"Clicking on element:{locator}")
        el = self.wait_for_clickable(locator)
        el.click()

    def input_password(self,locator, text):
        self.logger.debug(f"Inputting text '{text}' into element:{locator}")
        el = self.wait_for_visible(locator)
        #el.clear()
        for char in text:
            el.send_keys(char)
            time.sleep(0.01)



    def input_text(self,locator, text):
        self.logger.debug(f"Inputting text '{text}' into element:{locator}")
        el = self.wait_for_visible(locator)
        el.clear()
        el.send_keys(text)

    def get_element_text(self,locator):
        self.logger.debug(f"Getting text from element: {locator}")
        el = self.wait_for_visible( locator)
        return el.text.strip()

                ######################################
    #old one
    # def click_element(self, locator):
    #     self.wait.until(EC.element_to_be_clickable(locator)).click()

    # def input_text(self, locator, text):
    #     element=self.wait.until(EC.visibility_of_element_located(locator))
    #     element.clear()
    #     element.send_keys(text)

    # def get_element_text(self, locator):
    #     return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_Js_tooltipfor_invalidmail(self, locator):
        element= self.wait.until(EC.visibility_of_element_located(locator))
        validation_message = self.driver.execute_script("return arguments[0].validationMessage;", element)
        self.logger.debug(f"Getting text validation_message: {validation_message}")
        return validation_message

    def get_attribute(self, locator, attr):
        return self.wait.until(EC.visibility_of_element_located(locator)).get_attribute(attr)

    def is_element_enabled_clickable(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def is_element_visible_enabled(self,locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_enabled()
        except:
            return False

    def get_attribute_when_visible(self, locator, attribute_name):
        try:
            self.logger.debug(f"Waiting for element to be visible: {locator}")
            element = self.wait.until(EC.visibility_of_element_located(locator))
            attribute_value = element.get_attribute(attribute_name)
            self.logger.debug(f"Attribute '{attribute_name}' value: {attribute_value}")
            return attribute_value
        except TimeoutException:
            self.logger.exception(f"Element not visible: {locator}")
            raise
        except Exception as e:
            self.logger.exception(f"Failed to get attribute '{attribute_name}' from visible element {locator}: {e}")
            raise



