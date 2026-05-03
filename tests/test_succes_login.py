from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage

#information
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalilov"
zipcode="34000"

#1.Login
def test_success_login(driver):
        
        wait=WebDriverWait(driver,10)
        login_page=LoginPage(driver)
        login_page.login(username,password)

        inventory=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"inventory_list")))
        assert inventory.is_displayed(),"Inventory page did not load after login"
        assert "inventory" in driver.current_url

def test_add_product_to_cart(driver):
        wait=WebDriverWait(driver,10)
        login_page=LoginPage(driver).login(username,password)
        wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
        badge=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        
        assert badge.text =="1" , f'Expected cart count to be 1, but got {badge.text}'

def test_remove_product_from_cart(driver):
        wait=WebDriverWait(driver,10)
        login_page=LoginPage(driver).login(username,password)



        wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
        remove_btn=wait.until(ec.element_to_be_clickable((By.ID,"remove-sauce-labs-fleece-jacket")))
        remove_btn.click()
        # badge=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        # assert badge.text =="" , f'Expected cart count to be 1, but got {badge.text}'
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart badge should not be visible after removing product"

def test_reset_cart(driver):
        wait=WebDriverWait(driver,10)
        login_page=LoginPage(driver).login(username,password)


      

        wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
        wait.until(ec.element_to_be_clickable((By.ID,"react-burger-menu-btn"))).click()
        wait.until(ec.element_to_be_clickable((By.ID,"reset_sidebar_link"))).click()
        wait.until(ec.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        badges = driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        assert len(badges) == 0, "Cart should be empty after reset"


def test_checkout_without_zip(driver):
        wait=WebDriverWait(driver,10)

        login_page=LoginPage(driver).login(username,password)


        

        wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket"))).click()
        wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link"))).click()
        wait.until(ec.element_to_be_clickable((By.ID,"checkout"))).click()
        wait.until(ec.visibility_of_element_located((By.ID,"first-name"))).send_keys(firstname)
        wait.until(ec.visibility_of_element_located((By.ID,"last-name"))).send_keys(lastname)
        wait.until(ec.element_to_be_clickable((By.ID,"continue"))).click()
        error_msg=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"h3[data-test='error']")))
        assert "Error: Postal Code is required" in error_msg.text
        



        
        