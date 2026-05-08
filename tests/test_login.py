import pytest
from pages.login_page import LoginPage

@pytest.mark.login
@pytest.mark.parametrize(
        "username, password, error",
        [

                ("wrong_user", "wrong_pass", "Username and password do not match"),
                ("", "secret_sauce", "Username is required"),
                 ("standard_user", "", "Password is required"),

        ]

)

def test_invalid_login(driver,username,password,error):
        login=LoginPage(driver)
        login.login(username,password)
        assert error in login.get_error_message()
        # assert False
        

@pytest.mark.parametrize(
                "username,password",
                [
                       ("standard_user", "secret_sauce"), 
                       ("problem_user","secret_sauce"),
                       ("visual_user","secret_sauce"),

                ]
                

)
@pytest.mark.login
def test_successfull_login(driver,username,password):
        login=LoginPage(driver)
        login.login(username,password)
        assert "inventory" in driver.current_url, "Inventory page did not load after login"





        
        