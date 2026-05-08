import pytest
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from data.test_data import *

@pytest.mark.checkout
def test_checkout_without_zip(logged_in_inventory):
        inventory=logged_in_inventory
        inventory.add_product_to_cart(PRODUCT_JACKET)
        inventory.click_cart()

        cart=CartPage(inventory.driver)
        cart.click_checkout()
        
        checkout=CheckOutPage(inventory.driver)
        checkout.fill_checkout_info(firstname,lastname)
        checkout.click_continue()
        assert "Error: Postal Code is required" in checkout.get_error_message()