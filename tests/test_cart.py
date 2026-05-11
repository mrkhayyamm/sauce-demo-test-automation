import pytest
from pages.cart_page import CartPage
from utils.constants import *

@pytest.mark.cart
@pytest.mark.regression
@pytest.mark.all

def test_add_product_to_cart(logged_in_inventory):
 

        inventory=logged_in_inventory
        inventory.add_product_to_cart(PRODUCT_JACKET)
        cart=CartPage(inventory.driver)
        cart_count= cart.get_cart_badge_count()
        assert cart_count == "1", f'Expected cart count to be 1, but got {cart_count}'
   
    

@pytest.mark.cart
@pytest.mark.regression
@pytest.mark.all
def test_remove_product_from_cart(logged_in_inventory):
       

        inventory=logged_in_inventory
        inventory.add_product_to_cart(PRODUCT_JACKET)
        inventory.click_cart()
        cart=CartPage(inventory.driver)
        cart.remove_product_btn(PRODUCT_JACKET)
        assert cart.is_cart_empty()
        
@pytest.mark.cart
@pytest.mark.regression
@pytest.mark.all
def test_reset_cart(logged_in_inventory):
        inventory=logged_in_inventory
        inventory.add_product_to_cart(PRODUCT_JACKET)
        inventory.open_menu()
        inventory.click_reset()
        inventory.wait_until_cart_empty()
        assert inventory.is_cart_empty()

