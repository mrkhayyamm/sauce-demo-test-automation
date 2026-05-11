import pytest
from pages.login_page import LoginPage
from utils.data_reader import *
from utils.constants import *
from utils.logger import get_logger
logger = get_logger()


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.all
@pytest.mark.parametrize(
        "test_data",
        read_login_test_data()

)




def test_invalid_login(driver,test_data):
    
        logger.info("Starting invalid login test")
        login=LoginPage(driver)
        logger.info(f"trying login with username: {test_data['username']}")
        login.login(
                test_data["username"],
                test_data["password"]
        )
        actual_error=login.get_error_message()
        excepted_error=test_data["error"]

        if excepted_error not in actual_error:
                logger.error(f"Excepted error: {excepted_error}, but got {actual_error}")
        assert excepted_error in actual_error
        # assert test_data["error"] in login.get_error_message()
        logger.info("Invalid login test passed")
        

@pytest.mark.parametrize(
        "test_data",
        read_login_test_valid_data()

)
@pytest.mark.smoke
@pytest.mark.login
@pytest.mark.all
def test_successfull_login(driver,test_data):
        login=LoginPage(driver)
        login.login(
                test_data["username"],
                test_data["password"]

        )
        assert "inventory" in driver.current_url, "Inventory page did not load after login"





        
        