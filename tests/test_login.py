import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def test_saucedemo_title(driver):
    # Sayfa başlığının "Swag Labs" olup olmadığını kontrol etmeni istiyorum
    assert driver.title == "Swag Labs"

    time.sleep(1)


def test_positive_login_page(driver):
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    time.sleep(2)


    # DOĞRULAMA (ASSERTION) EKLEYELİM
    # Giriş yapınca karşımıza çıkan "Products" başlığını kontrol ediyoruz
    title_element = driver.find_element(By.XPATH, "//span[@class='title']")
    
    assert title_element.is_displayed(), "HATA: Ürünler başlığı görünmüyor!"
    assert title_element.text == "Products", f"HATA: Yanlış başlık! Gelen: {title_element.text}"

def test_positive_logout_page(driver):
    driver.find_element(By.ID, "react-burger-menu-btn").click() #burgermenuyu bulur
    WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, "bm-menu")))


    #logout sekmesi gelene kadar bekler
    logout_btn=WebDriverWait(driver,15).until(EC.visibility_of_element_located((By.ID, "logout_sidebar_link")))
    logout_btn.click() #logout butonuna tiklar



    assert driver.title == "Swag Labs"
    time.sleep(1)

    
    