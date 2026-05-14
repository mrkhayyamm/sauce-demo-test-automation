import pytest
from pages.login_page import LoginPage
from utils.data_reader import *
from utils.constants import *
from utils.logger import get_logger
import allure
  
   
logger = get_logger()

@allure.parent_suite("SauceDemo")
@allure.suite("Login Tests")
@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
@allure.feature("Login")
@allure.story("Invalid Login")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.parametrize(
        "test_data",
        read_login_test_data()

)




def test_invalid_login(driver,test_data):
    
        logger.info("Starting invalid login test")
        login=LoginPage(driver)
        logger.info(f"trying login with username: {test_data['username']}")
        with allure.step("Login with invalid credentials"):
                login.login(
                        test_data["username"],
                        test_data["password"]
                )
        with allure.step("Verify error message"):
                actual_error=login.get_error_message()
                expected_error=test_data["error"]

                if expected_error not in actual_error:
                        logger.error(f"Expected error: {expected_error}, but got {actual_error}")
                assert expected_error in actual_error
                # assert test_data["error"] in login.get_error_message()
                logger.info("Invalid login test passed")
                
        

@pytest.mark.parametrize(
        "test_data",
        read_login_test_valid_data()

)
@pytest.mark.smoke
@pytest.mark.login
@allure.feature("Login")
@allure.story("Successful Login")
@allure.severity(allure.severity_level.BLOCKER)
def test_successfull_login(driver,test_data):
        login=LoginPage(driver)
        with allure.step("Login with valid credentials"):
                login.login(
                        test_data["username"],
                        test_data["password"]

        )
        with allure.step("Verify inventory page opened"):
                assert "inventory" in driver.current_url, "Inventory page did not load after login"





        
        