
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLoginPositive:
    #TEST-1 SİTEYE GİRİŞ VE DOGRULAMA
    def test_saucedemo_title(self,driver):
        assert driver.title == "Swag Labs"

    #TEST-2 SİTEYE GİRİŞ YAPILIR USERNAME PASSWORD BİLGİSİ GİRİLİR
    def test_positive_login_page(self,driver):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
    # Giriş doğrulaması
        title_element = driver.find_element(By.XPATH, "//span[@class='title']")
        assert title_element.is_displayed(), "HATA: Ürünler Products görünmüyor!"
        assert title_element.text == "Products"


    #TEST-3 SİTEYE GİRİŞ YAPİLİR DOGRU BİLGİLER GİRİLİR TEKRARDAN ÇIKIŞ YAPILIR
    def test_positive_logout_page(self,driver):
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # login wait
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//span[@class='title']"))
        )

        # menu aç
        driver.find_element(By.ID, "react-burger-menu-btn").click()

        # logout butonunu bekle ve tıkla
        logout_btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))
        )
        logout_btn.click()

        # login sayfasını bekle
        onay = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        )

        assert onay.is_displayed(), "HATA!,ANA SAYFAYA DÖNMEDİ"