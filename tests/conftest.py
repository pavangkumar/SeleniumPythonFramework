
import allure
from allure_commons.types import AttachmentType
import pytest
from selenium import webdriver
from utilities.read_configurations import ReadConfig
from utilities.logger import get_logger
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.edge.options import Options
import os
from pytest_metadata.plugin import metadata_key
from  datetime import datetime

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Pytest hook to log test failures and capture screenshots if the driver fixture is available.
#     """
#     logger = get_logger("pytest_hook")
#     outcome = yield
#     rep = outcome.get_result()
#
#     if rep.when == "call" and rep.failed:
#         logger.error(f"Test failed: {item.name}")
#
#         # Optionally capture a screenshot
#         try:
#             driver_fixture = item.funcargs.get("driver")
#             if driver_fixture:
#                 screenshot_dir = os.path.join(os.getcwd(), "screenshots")
#                 os.makedirs(screenshot_dir, exist_ok=True)
#
#                 screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
#                 driver_fixture.save_screenshot(screenshot_path)
#
#                 logger.info(f"Saved screenshot to: {screenshot_path}")
#         except Exception:
#             logger.exception("Failed to capture screenshot on test failure")


@pytest.fixture(scope="class")
def setup_and_teardown(request):
    global driver
    driver = None
    browser = ReadConfig.get_browser().lower()
    if browser.__eq__("chrome"):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2  # 1: allow, 2: block
        })
        driver = webdriver.Chrome(options=chrome_options)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        edge_options = Options()
        # Block notifications
        edge_options.add_experimental_option("prefs", {
            "profile.default_content_setting_values.notifications": 2
        })
        edge_options.add_argument("--disable-notifications")
        edge_options.add_argument("--disable-infobars")
        edge_options.add_argument("--disable-popup-blocking")
        driver = webdriver.Edge(options=edge_options)
    else:
        driver = webdriver.Chrome()

    driver.maximize_window()
    driver.get(ReadConfig.get_base_url())
    request.cls.driver = driver
    # if request.cls is not None:
    #     request.cls.driver = driver
    yield driver
    driver.quit()

def pytest_addoption(parser):    # This will get the value from CLI /hooks
   parser.addoption("--browser")

# @pytest.fixture()
# def browser(request):  # This will return the Browser value to setup method
#    return request.config.getoption("--browser")

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
   config.stash[metadata_key]['Project Name'] = 'PracticeAutomation'
   config.stash[metadata_key]['Module Name'] = 'Login_Registration_Shop'
   config.stash[metadata_key]['Tester Name'] = 'Pavan'
# It is hook for delete/Modify Environment info to HTML Report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
  metadata.pop("Python", None)
  metadata.pop("Plugins", None)

# Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
   config.option.htmlpath = (
               os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime(
           "%d-%m-%Y %H-%M-%S") + ".html")