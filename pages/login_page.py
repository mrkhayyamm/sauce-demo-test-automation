from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
class LoginPage(BasePage):

    USERNAME=(By.ID,"user-name")
    PASSWORD=(By.ID,"password")
    LOGİN_BTN=(By.ID,"login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait=WebDriverWait(driver,10)

    def login(self, username, password):
        self.type(self.USERNAME,username)
        self.type(self.PASSWORD,password)
        self.click(self.LOGİN_BTN)

       