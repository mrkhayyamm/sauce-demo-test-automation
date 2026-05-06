from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckOutPage(BasePage):
    
    FİRST_NAME=(By.ID,"first-name")
    LAST_NAME=(By.ID, "last-name")
    ZIP_CODE=(By.ID,"postal-code")
    CONTINUE=(By.ID,"continue")
    ERROR_MSG=(By.CSS_SELECTOR, "h3[data-test='error']")
    def __init__(self, driver):
        super().__init__(driver)
        
    def fill_checkout_info(self,firstname,lastname,zipcode=None):
        self.type(self.FİRST_NAME,firstname)
        self.type(self.LAST_NAME,lastname)
        
        if zipcode:
            self.type(self.ZIP_CODE,zipcode)

    def click_continue(self):
        self.click(self.CONTINUE)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)


