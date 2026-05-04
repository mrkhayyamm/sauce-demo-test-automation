from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryPage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)
    
    def inventory_list(self):
       return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"inventory_list")))

    def add_product_to_cart(self,product_id):
        add_button_id= f'add-to-cart-{product_id}'
        self.wait.until(EC.element_to_be_clickable((By.ID,add_button_id))).click()
    

    def get_cart_badge_count(self):
        badge=self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_badge")))
        return badge.text
    
    def remove_product_btn(self,product_id):
        remove_btn_id=f'remove-{product_id}'
        remove_btn=self.wait.until(EC.element_to_be_clickable((By.ID,remove_btn_id)))
        remove_btn.click()

    def open_menu(self):
        burger_menu=self.wait.until(EC.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
        burger_menu.click()

    def click_reset(self):
           reset_side_bar=self.wait.until(EC.element_to_be_clickable((By.ID,"reset_sidebar_link")))
           reset_side_bar.click()

    def shopping_cart_button(self):
        shoping_cart=self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_link")))
        shoping_cart.click()

    def checkout_button(self):
        checkout= self.wait.until(EC.element_to_be_clickable((By.ID,"checkout")))
        checkout.click()
    def fill_checkout_info(self,firstname,lastname):
        self.wait.until(EC.visibility_of_element_located((By.ID,"first-name"))).send_keys(firstname)
        self.wait.until(EC.visibility_of_element_located((By.ID, "last-name"))).send_keys(lastname)

    def click_continue(self):
           self.wait.until(EC.element_to_be_clickable((By.ID,"continue"))).click()

    def get_error_message(self):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,"h3[data-test='error']"))).text
    
    # def is_cart_empty(self):
    #     badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
    #     return len(badges) == 0
    
    def wait_until_cart_empty(self):
        self.wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))

    
    def is_cart_empty(self):
        badges = self.driver.find_elements(By.CLASS_NAME, "shopping_cart_badge")
        return len(badges) == 0