from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
#
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalil"
zipcode="34000"

def test_e2e_shopping_workflow(driver):
    wait=WebDriverWait(driver,10)

    #go to the webiste, insert correct login and password and click to login button
    driver.find_element(By.ID,"user-name").send_keys(username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    #choose the product

    add_btn=wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-fleece-jacket")))
    add_btn.click()

    cart_link=driver.find_element(By.XPATH, "//a[@data-test='shopping-cart-link']")
    cart_link.click()


    #assert choosen product
    product=wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@data-test='inventory-item-name']")))
    assert product.text =="Sauce Labs Fleece Jacket"
   
    #filling out the order form
    driver.find_element(By.XPATH, "//button[@data-test='checkout']").click()

    first_name_input=wait.until(EC.visibility_of_element_located((By.ID, "first-name")))
    first_name_input.send_keys(firstname)

    driver.find_element(By.ID, "last-name").send_keys(lastname)  
    driver.find_element(By.ID, "postal-code").send_keys(zipcode)
    driver.find_element(By.ID, "continue").click()
    
    #Price Check
    pricecheck=wait.until(EC.visibility_of_element_located((By.XPATH,"//div[@data-test='total-label']")))
    assert "53.99" in pricecheck.text

    #order message check
    driver.find_element(By.XPATH, "//button[@data-test='finish']").click()
    ordermessage=wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@data-test='complete-header']")))
    assert ordermessage.text == "Thank you for your order!"
     
    #back home
    driver.find_element(By.ID, "back-to-products").click()
    assert wait.until(EC.url_contains(("inventory.html")))


    