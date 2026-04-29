from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
#information
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalilov"
zipcode="34000"


class TestAll:
    def test_comprehensive(self,driver):
 #1.Login
        username_field=driver.find_element(By.ID, "user-name")
        username_field.send_keys(username)

        password_field=driver.find_element(By.ID, "password")
        password_field.send_keys(password)

        login_button=driver.find_element(By.ID,"login-button")
        login_button.click()

#2.Change dropdown
        select=Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
        select.select_by_value("hilo")
#3. Add All Products
        Fleece_jacket=driver.find_element(By.ID,"add-to-cart-sauce-labs-fleece-jacket")
        Fleece_jacket.click()

        Labs_backpack=driver.find_element(By.ID,"add-to-cart-sauce-labs-backpack")
        Labs_backpack.click()

        Bolt_Tshirt=driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        Bolt_Tshirt.click()


        Red_tshirt=driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        Red_tshirt.click()


        Bike_light=driver.find_element(By.ID,"add-to-cart-sauce-labs-bike-light")
        Bike_light.click()


        Onesie=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        Onesie.click()
#4.Check Cart
        cart_button=driver.find_element(By.CLASS_NAME,"shopping_cart_badge")
        cart_count=cart_button.text
        assert cart_count =="6", f"cart count must be 6, but gived {cart_count}"
        cart_button.click()


#5.Continue Shopping
        continue_shopping= driver.find_element(By.ID,"continue-shopping")
        continue_shopping.click()

#6.Hamburger menu
        hamburger_menu=driver.find_element(By.ID,"react-burger-menu-btn")
        hamburger_menu.click()
        time.sleep(2)

#7.Reset
        reset_button=driver.find_element(By.ID,"reset_sidebar_link")
        reset_button.click()


#8.Refresh Page
        driver.refresh()
#9.Check Cart Count
        cart_button2=driver.find_element(By.CLASS_NAME,"shopping_cart_link")
        cart_count2=cart_button2.text
        assert cart_count2 =="", f"cart count must be 0, but gived {cart_count2}"
     
        

#10. DropDown and click Z to A
        select=Select(driver.find_element(By.CLASS_NAME,"product_sort_container"))
        select.select_by_value("za")

#11. Add Products to Cart
        Onesie=driver.find_element(By.ID,"add-to-cart-sauce-labs-onesie")
        Onesie.click()

        Red_tshirt=driver.find_element(By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")
        Red_tshirt.click()

        Bolt_Tshirt=driver.find_element(By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")
        Bolt_Tshirt.click()

#12.Go to the Cart
        cart_button2.click()

#13.Remove Prod from Cart
        driver.find_element(By.ID,"remove-sauce-labs-onesie").click()

#14.Check-out
        check_out_btn=driver.find_element(By.ID,"checkout")
        check_out_btn.click()
        

#15.Cancel
        cancel_btn=driver.find_element(By.ID,"cancel")
        cancel_btn.click()

#16.Remove prod
        driver.find_element(By.ID,"remove-sauce-labs-bolt-t-shirt").click()

#17.Check-out
        check_out_btn=driver.find_element(By.ID,"checkout")
        check_out_btn.click()

#18.Fill-out the Form
        fname=driver.find_element(By.ID,"first-name")
        fname.send_keys(firstname)

        lname=driver.find_element(By.ID,"last-name")
        lname.send_keys(lastname)

#19.Continue
        continue_page=driver.find_element(By.ID,"continue")
        continue_page.click()

#20.Assert Error Msg
        error_element=driver.find_element(By.CSS_SELECTOR,"h3[data-test='error']")
        error_msg=error_element.text
        assert error_msg=="Error: Postal Code is required"

#21.Fill-out the Form again
        fname.clear()
        fname=driver.find_element(By.ID,"first-name")
        fname.send_keys(firstname)

        lname.clear()
        lname=driver.find_element(By.ID,"last-name")
        lname.send_keys(lastname)

        zipp=driver.find_element(By.ID,"postal-code")
        zipp.send_keys(zipcode)

#22.Continue Again
        continue_page.click()

#23.Check Total Price
        total_price=driver.find_element(By.CLASS_NAME,"summary_total_label")
        total_price_msg= total_price.text
        assert total_price_msg =="Total: $25.90"

#24.Finish
        finish_btn=driver.find_element(By.ID,"finish")
        finish_btn.click()

#25. Assert order messag
        order=driver.find_element(By.CLASS_NAME,"complete-header")
        order_msg=order.text
        assert order_msg=="Thank you for your order!"

#26. Back to home page
        back_home_btn=driver.find_element(By.ID,"back-to-products")
        back_home_btn.click()

#27.Hamburger menu Again
        hamburger_menu=driver.find_element(By.ID,"react-burger-menu-btn")
        hamburger_menu.click()
        time.sleep(2)

#28.Logout
        log_out_btn=driver.find_element(By.ID,"logout_sidebar_link")
        log_out_btn.click()

#29. Assert Home page
        home_page=driver.find_element(By.XPATH,"//h4[contains(text(), 'Accepted usernames are')]")
        home_page_msg=home_page.text
        assert home_page_msg== "Accepted usernames are:"










