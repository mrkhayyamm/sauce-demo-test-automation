
from utils.constants import *
from pages.cart_page import CartPage
from pages.checkout_page import CheckOutPage
from utils.data_reader import read_checkout_data
import pytest


@pytest.mark.parametrize(
    "test_data",
    read_checkout_data()
)

@pytest.mark.checkout
@pytest.mark.regression
def test_checkout_without_zip(logged_in_inventory, test_data):

    inventory = logged_in_inventory

    inventory.add_product_to_cart(PRODUCT_JACKET)
    inventory.click_cart()

    cart = CartPage(inventory.driver)
    cart.click_checkout()

    checkout = CheckOutPage(inventory.driver)

    checkout.fill_checkout_info(
        test_data["firstname"],
        test_data["lastname"]
    )

    checkout.click_continue()

    assert "Error: Postal Code is required" in checkout.get_error_message()