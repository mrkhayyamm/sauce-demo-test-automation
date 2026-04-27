from selenium.webdriver.common.by import By

username = "standard_user"
password = "secret_sauce"

class TestInventory:

    def test_inventory(self, driver):

        # login
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

        items = driver.find_elements(By.CLASS_NAME, "inventory_item")

        assert len(items) == 6

        for item in items:
            name = item.find_element(By.CLASS_NAME, "inventory_item_name").text
            price = item.find_element(By.CLASS_NAME, "inventory_item_price").text
            img = item.find_element(By.TAG_NAME, "img")

            assert name != ""
            assert price != ""
            assert img.is_displayed()


       