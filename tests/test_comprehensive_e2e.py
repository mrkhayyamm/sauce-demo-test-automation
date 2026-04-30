from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

#information
username="standard_user"
password="secret_sauce"
firstname="Khayyam"
lastname="Khalilov"
zipcode="34000"


class TestAll:
    
 #1.Login
      def test_login(self,driver):
        
        wait=WebDriverWait(driver,10)
        username_field=wait.until(ec.visibility_of_element_located((By.ID,"user-name")))
        username_field.send_keys(username)

        password_field=wait.until(ec.visibility_of_element_located((By.ID,"password")))
        password_field.send_keys(password)

        login_button=wait.until(ec.element_to_be_clickable((By.ID,"login-button")))
        login_button.click()

#2.Change dropdown
        select=Select(wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))))
        select.select_by_value("hilo")
#3. Add All Products (BU KISIMA TEKRAR BAK)
        Fleece_jacket=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-fleece-jacket")))
        Fleece_jacket.click()

        Labs_backpack= wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-backpack")))
        Labs_backpack.click()

        Bolt_Tshirt= wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")))
        Bolt_Tshirt.click()


        Red_tshirt=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        Red_tshirt.click()


        Bike_light= wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bike-light")))
        Bike_light.click()


        Onesie=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie")))
        Onesie.click()
#4.Check Cart
        cart_button=wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"shopping_cart_badge")))
        cart_count=cart_button.text
        assert cart_count =="6", f"cart count must be 6, but got {cart_count}"
        cart_button.click()


#5.Continue Shopping
        continue_shopping= wait.until(ec.element_to_be_clickable((By.ID,"continue-shopping")))
        continue_shopping.click()

#6.Hamburger menu
        hamburger_menu=wait.until(ec.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
        hamburger_menu.click()


#7.Reset
        reset_button=wait.until(ec.element_to_be_clickable((By.ID,"reset_sidebar_link")))
        reset_button.click()


#8.Refresh Page
        driver.refresh()
        wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"inventory_list")))
#9.Check Cart Count
        cart_button2=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"shopping_cart_link")))
        cart_count2=cart_button2.text
        assert cart_count2 =="", f"cart count must be 0, but got {cart_count2}"
     
        

#10. DropDown and click Z to A
        select=Select(wait.until(ec.element_to_be_clickable((By.CLASS_NAME,"product_sort_container"))))
        select.select_by_value("za")

#11. Add Products to Cart
        Onesie=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-onesie")))
        Onesie.click()

        Red_tshirt=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-test.allthethings()-t-shirt-(red)")))
        Red_tshirt.click()

        Bolt_Tshirt=wait.until(ec.element_to_be_clickable((By.ID,"add-to-cart-sauce-labs-bolt-t-shirt")))
        Bolt_Tshirt.click()

#12.Go to the Cart
        cart_button2.click()

#13.Remove Prod from Cart
        wait.until(ec.element_to_be_clickable((By.ID,"remove-sauce-labs-onesie"))).click()

#14.Check-out
        check_out_btn=wait.until(ec.element_to_be_clickable((By.ID,"checkout")))
        check_out_btn.click()
        

#15.Cancel
        cancel_btn=wait.until(ec.element_to_be_clickable((By.ID,"cancel")))
        cancel_btn.click()

#16.Remove prod
        wait.until(ec.element_to_be_clickable((By.ID,"remove-sauce-labs-bolt-t-shirt"))).click()

#17.Check-out
        check_out_btn=wait.until(ec.element_to_be_clickable((By.ID,"checkout")))
        check_out_btn.click()

#18.Fill-out the Form
        fname=wait.until(ec.visibility_of_element_located((By.ID,"first-name")))
        fname.send_keys(firstname)

        lname=wait.until(ec.visibility_of_element_located((By.ID,"last-name")))
        lname.send_keys(lastname)

#19.Continue
        continue_page=wait.until(ec.element_to_be_clickable((By.ID,"continue")))
        continue_page.click()

#20.Assert Error Msg
        error_element=wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR,"h3[data-test='error']")))
        error_msg=error_element.text
        assert "Postal Code is required"in error_msg

#21.Fill-out the Form again
        fname.clear()
        fname=wait.until(ec.visibility_of_element_located((By.ID,"first-name")))
        fname.send_keys(firstname)

        lname.clear()
        lname=wait.until(ec.visibility_of_element_located((By.ID,"last-name")))
        lname.send_keys(lastname)

        zipp=wait.until(ec.visibility_of_element_located((By.ID,"postal-code")))
        zipp.send_keys(zipcode)

#22.Continue Again
        wait.until(ec.element_to_be_clickable((By.ID,"continue"))).click()
        

#23.Check Total Price
        total_price=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"summary_total_label")))
        total_price_msg= total_price.text
        assert total_price_msg =="Total: $17.27"

#24.Finish
        finish_btn=wait.until(ec.element_to_be_clickable((By.ID,"finish")))
        finish_btn.click()

#25. Assert order messag
        order=wait.until(ec.visibility_of_element_located((By.CLASS_NAME,"complete-header")))
        order_msg=order.text
        assert order_msg=="Thank you for your order!"

#26. Back to home page
        back_home_btn=wait.until(ec.element_to_be_clickable((By.ID,"back-to-products")))
        back_home_btn.click()

#27.Hamburger menu Again
        hamburger_menu=wait.until(ec.element_to_be_clickable((By.ID,"react-burger-menu-btn")))
        hamburger_menu.click()

#28.Logout
        log_out_btn=wait.until(ec.element_to_be_clickable((By.ID,"logout_sidebar_link")))
        log_out_btn.click()

#29. Assert Home page
        home_page=wait.until(ec.visibility_of_element_located((By.XPATH,"//h4[contains(text(), 'Accepted usernames are')]")))
        home_page_msg=home_page.text
        assert "Accepted usernames are:" in home_page_msg

      
            
           










