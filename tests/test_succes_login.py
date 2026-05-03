from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

#information
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalilov"
zipcode="34000"


#1.Login
def test_success_login(driver):
        login_page=LoginPage(driver)
        login_page.login(username,password)
        inventory_page=InventoryPage(driver)
        inventorylist= inventory_page.inventory_list()
        assert inventorylist.is_displayed(),"Inventory page did not load after login"
        assert "inventory" in driver.current_url

def test_add_product_to_cart(driver):
        login_page=LoginPage(driver)
        login_page.login(username,password)
        inventory_page=InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")
        cart_count=inventory_page.get_cart_badge_count()
        assert cart_count=="1" , f'Expected cart count to be 1, but got {cart_count}'

def test_remove_product_from_cart(driver):
        login_page=LoginPage(driver)
        login_page.login(username,password)
        inventory_page=InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory_page.remove_product_btn("sauce-labs-fleece-jacket")
        assert inventory_page.is_cart_empty()

def test_reset_cart(driver):
        login_page=LoginPage(driver)
        login_page.login(username,password)
        inventory_page=InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory_page.open_menu()
        inventory_page.click_reset()
        inventory_page.wait_until_cart_empty()
        assert inventory_page.is_cart_empty()



def test_checkout_without_zip(driver):
        login_page=LoginPage(driver)
        login_page.login(username,password)
        inventory_page=InventoryPage(driver)
        inventory_page.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory_page.shopping_cart_button()
        inventory_page.checkout_button()
        inventory_page.fill_checkout_info(firstname,lastname)
        inventory_page.click_continue()
        error_msg=inventory_page.get_error_message()
        assert "Error: Postal Code is required" in error_msg
        



        
        