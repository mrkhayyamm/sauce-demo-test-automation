import pytest
import os
import base64
from datetime import datetime
from pytest_html import extras
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from config.config import *
import time
import uuid
import allure
from allure_commons.types import AttachmentType
timestamp = int(time.time())
username = "standard_user"
password = "secret_sauce"









 

@pytest.fixture(scope="function")
def driver():
    options = Options()

    # Browser settings
    options.add_argument("--incognito")

    # Headless mode
    if HEADLESS:
        options.add_argument("--headless=new")

    # CI/CD stability
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")

    # Faster execution
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")


    if BROWSER =="chrome":

        driver = webdriver.Chrome(options=options)
    else:
            raise ValueError("Unsupported browser")
    

    driver.get(BASE_URL)
 

    yield driver
    driver.quit()


















@pytest.fixture()
def logged_in_inventory(driver):
    login_page=LoginPage(driver)
    login_page.login(username,password)
    inventory_page=InventoryPage(driver)
    return inventory_page



@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            # SCREENSHOTS FOLDER
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            screenshot_file = f"{uuid.uuid4()}.png"
            screenshot_path = os.path.join(screenshots_dir, screenshot_file)

            driver.save_screenshot(screenshot_path)

            # PYTEST-HTML SCREENSHOT
            with open(screenshot_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])

            extra.append(
                extras.html(
                    f'<div><img src="data:image/png;base64,{encoded_image}" '
                    f'style="width:600px;height:auto;border:1px solid #ccc;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
            )

            report.extra = extra

            # ALLURE SCREENSHOT
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=AttachmentType.PNG
            )

            # ALLURE LOG ATTACHMENT
            if os.path.exists("logs/test.log"):

                with open("logs/test.log", "r") as log_file:

                    allure.attach(
                        log_file.read(),
                        name="test_log",
                        attachment_type=AttachmentType.TEXT
                    )


