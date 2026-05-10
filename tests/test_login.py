import pytest
from pages.login_page import LoginPage
from utils.data_reader import *
from utils.constants import *

@pytest.mark.regression
@pytest.mark.login
@pytest.mark.negative
@pytest.mark.parametrize(
        "test_data",
        read_login_test_data()

)



def test_invalid_login(driver,test_data):
        login=LoginPage(driver)
        login.login(
                test_data["username"],
                test_data["password"]
        )
        assert test_data["error"] in login.get_error_message()
        # assert False
        

@pytest.mark.parametrize(
        "test_data",
        read_login_test_valid_data()

)
@pytest.mark.smoke
@pytest.mark.login
def test_successfull_login(driver,test_data):
        login=LoginPage(driver)
        login.login(
                test_data["username"],
                test_data["password"]

        )
        assert "inventory" in driver.current_url, "Inventory page did not load after login"





        
        