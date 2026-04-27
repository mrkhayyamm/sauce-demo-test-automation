from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

username = "standard_user"
password = "secret_sauce"

class TestSorting:

    def test_sort_price_low_to_high(self, driver):
     # login
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        select= Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
        select.select_by_value("lohi")
        
        time.sleep(1)
        
        price_elements=driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices=[]
        for price in price_elements:
            value=float(price.text.replace("$", ""))
            prices.append(value)

        assert len(prices) > 0, "Fiyat listesi boş"
        assert prices == sorted(prices), f"Fiyatlar sıralı değil: {prices}"


