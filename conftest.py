import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
username = "standard_user"
password = "secret_sauce"

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--incognito")  # Gizli modda aç
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.saucedemo.com/")
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
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_name = f"screenshots/{item.name}_{timestamp}.png"

            driver.save_screenshot(screenshot_name)




 




    