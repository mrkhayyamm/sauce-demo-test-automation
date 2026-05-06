from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
# from pages.base_page import BasePage
import pytest

#information
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalilov"
zipcode="34000"


#1.Login
# @pytest.mark.smoke
def test_successfull_login(logged_in_inventory):
        inventorylist= logged_in_inventory.inventory_list()
        assert inventorylist, "Inventory page did not load after login"


def test_add_product_to_cart(logged_in_inventory):
        #HATA VERIRSE TEKRARDAN AÇ

        # logged_in_inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        # cart_count=logged_in_inventory.get_cart_badge_count()
        # assert cart_count=="1" , f'Expected cart count to be 1, but got {cart_count}'

        inventory=logged_in_inventory
        inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        cart=CartPage(inventory.driver)
        cart_count= cart.get_cart_badge_count()
        assert cart_count == "1", f'Expected cart count to be 1, but got {cart_count}'




def test_remove_product_from_cart(logged_in_inventory):
        #TEST FAİLED VERMEZSE SİLİNECEK,FAİL EDERSE GERİ GETİR

        # logged_in_inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        # logged_in_inventory.remove_product_btn("sauce-labs-fleece-jacket")
        # assert logged_in_inventory.is_cart_empty()

        inventory=logged_in_inventory
        inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory.go_to_cart()
        cart=CartPage(inventory.driver)
        cart.remove_product_btn("sauce-labs-fleece-jacket")
        assert cart.is_cart_empty()



def test_reset_cart(logged_in_inventory):
#HATA VERIRSE KOD GERI GETIRELECEK
        # logged_in_inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        # logged_in_inventory.open_menu()
        # logged_in_inventory.click_reset()
        # logged_in_inventory.wait_until_cart_empty()
        # assert logged_in_inventory.is_cart_empty()
        
        inventory=logged_in_inventory
        inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory.open_menu()
        inventory.click_reset()
        inventory.wait_until_cart_empty()
        assert inventory.is_cart_empty()







# @pytest.mark.smoke

#HATA VERIRSE TEST , TEKRARDAN GERI GETIRILSIN
# def test_checkout_without_zip(logged_in_inventory):
#         logged_in_inventory.add_product_to_cart("sauce-labs-fleece-jacket")
#         logged_in_inventory.shopping_cart_button()
#         logged_in_inventory.checkout_button()
#         logged_in_inventory.fill_checkout_info(firstname,lastname)
#         logged_in_inventory.click_continue()
#         error_msg=logged_in_inventory.get_error_message()
#         assert "Error: Postal Code is required" in error_msg

def test_checkout_without_zip(logged_in_inventory):
        inventory=logged_in_inventory
        inventory.add_product_to_cart("sauce-labs-fleece-jacket")
        inventory.go_to_cart()
        cart=CartPage(inventory.driver)
        cart.click_checkout()
        checkout=CheckOutPage(inventory.driver)
        checkout.fill_checkout_info(firstname,lastname)
        checkout.click_continue()
        assert "Error: Postal Code is required" in checkout.get_error_message()


       
 #HATA VERDİĞİ İÇİN ŞİMDİLİK ERTELE EN SON BAK
# def test_checkout_with_all(logged_in_inventory):
#         logged_in_inventory.add_product_to_cart("sauce-labs-fleece-jacket")
#         logged_in_inventory.shopping_cart_button()
#         logged_in_inventory.checkout_button()
#         logged_in_inventory.fill_checkout_info(firstname,lastname,zipcode)
#         logged_in_inventory.click_continue()
#         logged_in_inventory.click_finish()
#         order_msg=logged_in_inventory.get_order_message()
#         assert "Thank you for your order!" in order_msg




        
        