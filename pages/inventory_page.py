from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class InventoryPage(BasePage):
    INVENTORY_LIST=(By.CLASS_NAME,"inventory_list")
    CART_BADGE=(By.CLASS_NAME,"shopping_cart_badge")
    MENU_BTN=(By.ID,"react-burger-menu-btn")
    RESET_BTN=(By.ID,"reset_sidebar_link")
    CART_BTN=(By.CLASS_NAME,"shopping_cart_link")
    # CHECKOUT_BTN=(By.ID,"checkout")
    # FİRST_NAME=(By.ID,"first-name")
    # LAST_NAME=(By.ID, "last-name")
    # ZIP_CODE=(By.ID,"postal-code")
    # CONTINUE=(By.ID,"continue")
    # ERROR_MSG=(By.CSS_SELECTOR, "h3[data-test='error']")
    FINISH=(By.ID,"finish")
    ORDER_MSG=(By.CLASS_NAME,"complete-header")


    def __init__(self, driver):
        super().__init__(driver)


    def go_to_cart(self):
        self.click(self.CART_BTN)

    def inventory_list(self):
        return self.driver.find_elements(*self.INVENTORY_LIST)
    
    def is_inventory_loaded(self):
       return self.is_visible(self.INVENTORY_LIST)

    def add_product_to_cart(self,product_id):
        locator= (By.ID, f"add-to-cart-{product_id}")
        self.click(locator)
    
    #KOD HATA VERIRSE AÇ BUNU
    # def get_cart_badge_count(self):
    #     return self.get_text(self.CART_BADGE)
    
    # def remove_product_btn(self,product_id):
    #     locator = (By.ID, f"remove-{product_id}")
    #     self.click(locator)
    
    def open_menu(self):
        self.click(self.MENU_BTN)

    def click_reset(self):
           self.click(self.RESET_BTN)

    def shopping_cart_button(self):
        self.click(self.CART_BTN)

    # def checkout_button(self):
    #     self.click(self.CHECKOUT_BTN)

#hata verırse ac
    # def fill_checkout_info(self,firstname,lastname):

    #     self.type(self.FİRST_NAME,firstname)
    #     self.type(self.LAST_NAME,lastname)

        # self.type(self.ZIP_CODE,zipcode)

    # def click_continue(self):
    #        self.click(self.CONTINUE)

    # def get_error_message(self):
   
    #     return self.get_text(self.ERROR_MSG)
    
    def wait_until_cart_empty(self):
        self.wait_invisible(self.CART_BADGE)

    
    def is_cart_empty(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return len(badges) == 0

    def click_finish(self):
        self.click(self.FINISH)
    
    def get_order_message(self):
        return self.get_text(self.ORDER_MSG)