from selenium.webdriver.common.by import By

class TestCart:
    def test_cart_checking(self,driver):
        username="standard_user"
        password="secret_sauce"
         # login
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.ID, "password").send_keys(password)
        driver.find_element(By.ID, "login-button").click()

     # add product to cart
        driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        cart_badge=driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
        cart_badge_count= cart_badge.text
        assert cart_badge.is_displayed()
        assert cart_badge_count=="1", f"Beklenen 1, ama gelen: {cart_badge_count}"
