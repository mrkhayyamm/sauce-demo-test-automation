from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckOutPage(BasePage):
    
    FIRST_NAME=(By.ID,"first-name")
    LAST_NAME=(By.ID, "last-name")
    ZIP_CODE=(By.ID,"postal-code")
    CONTINUE=(By.ID,"continue")
    ERROR_MSG=(By.CSS_SELECTOR, "h3[data-test='error']")
    ORDER_MSG=(By.CLASS_NAME,"complete-header")
    FINISH=(By.ID,"finish")


    
    def __init__(self, driver):
        super().__init__(driver)
        
    def fill_checkout_info(self,firstname,lastname,zipcode=None):
        self.type(self.FIRST_NAME,firstname)
        self.type(self.LAST_NAME,lastname)
        
        if zipcode:
            self.type(self.ZIP_CODE,zipcode)

    def click_continue(self):
        self.click(self.CONTINUE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)
    
    def get_order_message(self):
        return self.get_text(self.ORDER_MSG)
    
    def click_finish(self):
        self.click(self.FINISH)

