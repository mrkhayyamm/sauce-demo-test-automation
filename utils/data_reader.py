import json

def read_login_test_data():
    with open("data/invalid-login-data.json") as file:
        return json.load(file)

def read_login_test_valid_data():
    with open("data/valid-login-data.json") as file:
        return json.load(file)

def read_checkout_data():
    with open("data/checkout-data.json") as file:
        return json.load(file)
        

