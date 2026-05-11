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
timestamp = int(time.time())
username = "standard_user"
password = "secret_sauce"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--incognito")  # Gizli modda aç

    if HEADLESS:
        options.add_argument("--headless=new")


    if BROWSER =="chrome":

        driver = webdriver.Chrome(options=options)
    else:
            raise ValueError("Unsupported browser")
    

    driver.get(BASE_URL)
    driver.maximize_window()

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

            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

            screenshot_file = f"{uuid.uuid4()}.png"

            screenshot_path = os.path.join(screenshots_dir, screenshot_file)

            driver.save_screenshot(screenshot_path)

            with open(screenshot_path, "rb") as image_file:
                encoded_image = base64.b64encode(image_file.read()).decode()

            extra = getattr(report, "extra", [])

            extra.append(
                extras.html(
                    f'<div><img src="data:image/png;base64,{encoded_image}" '
                    f'style="width:600px;height:auto;border:1px solid #ccc;";" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
            )

            report.extra = extra


