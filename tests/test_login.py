import pytest
from pages.login_page import LoginPage
from utils.data_reader import *
from utils.constants import *
#PAZARTESİ İÇİN NOT
#SORUNLAR TAM ÇÖZÜLMEDİĞİ İÇİN GİT PUSH YAPILMADI
#LOGIN VE CHECKOUT SAYFALARI SORUNLU NAME FIRSTANME NASIL KULLANILMALI ONU HALL ETMEK LAZIM

@pytest.mark.login
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
@pytest.mark.login
@pytest.mark.deneme
def test_successfull_login(driver,test_data):
        login=LoginPage(driver)
        login.login(
                test_data["username"],
                test_data["password"]

        )
        assert "inventory" in driver.current_url, "Inventory page did not load after login"





        
        