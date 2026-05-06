from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def click(self,locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def type(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)

    def get_text(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text
    
    
    def wait_invisible(self,locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

    def find(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))
        
    def is_visible(self,locator):
       return  self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
    
    # def is_visible(self,locator):
    #     try:
    #         self.find(locator).is_displayed
    #     except:
    #         False

    def is_present(self,locator):
        return len(self.driver.find_elements(*locator))>0
    
    def send_keys(self,locator,text):
        self.wait.until(EC.visibility_of_element_located(locator)).send_keys(text)