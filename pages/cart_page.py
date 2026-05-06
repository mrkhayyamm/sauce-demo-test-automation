from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CHECKOUT_BTN=(By.ID,"checkout")
    CART_BADGE=(By.CLASS_NAME,"shopping_cart_badge")
    
    def __init__(self, driver):
        super().__init__(driver)
   
    def remove_product_btn(self,product_id):
        locator = (By.ID, f"remove-{product_id}")
        self.click(locator)

    def click_checkout(self):
        self.click(self.CHECKOUT_BTN)

    def is_cart_empty(self):
        badges = self.driver.find_elements(*self.CART_BADGE)
        return len(badges) == 0
    
    
    def get_cart_badge_count(self):
        return self.get_text(self.CART_BADGE)