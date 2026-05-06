import pytest
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





 




    