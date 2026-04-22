import pytest
from selenium import webdriver

@pytest.fixture (scope="session") #bu testimizin kapanmadan devam etmesini sağlar
def driver():
    driver = webdriver.Chrome() #guncel selenıumlarda boyle kısa şekilde yazmak yeterlidir
    driver.get("https://www.saucedemo.com/") #test edeceğimiz sitenin linki
    driver.maximize_window() #site açıldıktan sonra tam ekran yapar

    yield driver
    driver.quit() # ram tasarrufu için kapatmak şart