from selenium.webdriver.common.by import By
username="dasda"
password="asdasd"

class TestLoginNegative:

    def test_negative_login(self,driver):
        driver.find_element(By.ID, "user-name").send_keys(username)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
        driver.find_element(By.ID, "login-button").click()
        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.is_displayed()
        assert error_message.text == "Epic sadface: Username and password do not match any user in this service"

        
    def test_negative_login_empty_password(self,driver):
        username2=""
        password2=""
        # Sayfayı yenileyelim ki önceki testten kalan veriler temizlensin
        driver.refresh() 
        
        driver.find_element(By.ID, "user-name").send_keys(username2)
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password2)
        # Şifre alanını boş bırakıyoruz
        driver.find_element(By.ID, "login-button").click()

        error_message = driver.find_element(By.XPATH, "//h3[@data-test='error']")
        assert error_message.text == "Epic sadface: Username is required"
                                 