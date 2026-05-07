from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    INVENTORY_LIST=(By.CLASS_NAME,"inventory_list")
    CART_BADGE=(By.CLASS_NAME,"shopping_cart_badge")
    MENU_BTN=(By.ID,"react-burger-menu-btn")
    RESET_BTN=(By.ID,"reset_sidebar_link")
    CART_BTN=(By.CLASS_NAME,"shopping_cart_link")
   


    def __init__(self, driver):
        super().__init__(driver)


    def click_cart(self):
        self.click(self.CART_BTN)

    
    def is_inventory_loaded(self):
       return self.is_visible(self.INVENTORY_LIST)

    def add_product_to_cart(self,product_id):
        locator= (By.ID, f"add-to-cart-{product_id}")
        self.click(locator)
    
    
    def open_menu(self):
        self.click(self.MENU_BTN)

    def click_reset(self):
           self.click(self.RESET_BTN)


    def wait_until_cart_empty(self):
        self.wait_invisible(self.CART_BADGE)

    
    def is_cart_empty(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return len(badges) == 0
    
