import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

from src.web.setup import SetupWeb
import logging


class order_page:
    def __init__ (self) :
        self.logger = logging.getLogger("TestLogger")  # Using the same logger as in conftest.py
        self.logger.setLevel(logging.INFO)

    def click_load_products(self, driver : webdriver.Chrome):
        """Extract the list of deposits from the deposit table."""
        try:
            # Wait for the table to be visible and load completely
            time.sleep(5)
            edit_button = driver.find_element(By.ID, "searchinput_products")
            edit_button.click()
            self.logger.info("load_products clicked")
            time.sleep(5)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")


    def write_product_name(self, driver : webdriver.Chrome, product):
        """Extract the list of deposits from the deposit table."""
        try:

            driver.find_element(By.ID, "searchInput_products").send_keys(product)
            
            time.sleep(2)
            
        except Exception as e:
            self.logger.error(f"Error while extracting deposit list: {e}")
    
    def add_product(self, driver : webdriver.Chrome, product):
        try:

            driver.find_element(By.XPATH, f"//div[@class='products_view' and contains(., '{product}')]").click()
            self.logger.info("Argan oil soap")
            time.sleep(2)
            
        except Exception as e:
            self.logger.error(f"Error while extracting deposit list: {e}")
    
    def write_quantity(self, driver : webdriver.Chrome, quantity: int):
        try:
                    # quantity
            qte = driver.find_element(By.ID, "quantity")
            qte.send_keys(quantity)
            time.sleep(2)
            self.logger.info("done")
            
        except Exception as e:
            self.logger.error(f"Error while extracting deposit list: {e}")

    def click_add(self, driver : webdriver.Chrome):
        try:
            driver.find_element(By.ID, "add").click()
            time.sleep(2)
            
        except Exception as e:
            self.logger.error(f"Error while extracting deposit list: {e}")

    def select_carrier(self, driver : webdriver.Chrome):
        """Extract the list of deposits from the deposit table."""
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-addDeliveryType-container").click()
            
            self.logger.info("okdelivery select clicked")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")
        
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            # data-select2-id="select2-addDeliveryType-result-e2mh-1"
            edit_button = driver.find_element(By.CLASS_NAME, "select2-search__field")
            edit_button.send_keys("carrier")
            edit_button.send_keys(Keys.ENTER)
            
            
            self.logger.info("carrier selected ")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")


    def select_head_office(self, driver : webdriver.Chrome):
        """Extract the list of deposits from the deposit table."""
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-addDeliveryType-container").click()
            
            self.logger.info("delivery select clicked")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")
        
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            # data-select2-id="select2-addDeliveryType-result-e2mh-1"
            edit_button = driver.find_element(By.CLASS_NAME, "select2-search__field")
            edit_button.send_keys("head office")
            edit_button.send_keys(Keys.ENTER)
            
            
            self.logger.info("head office selected ")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")


    def select_agency(self, driver : webdriver.Chrome):
        """Extract the list of deposits from the deposit table."""
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-addDepot-container").click()
            
            self.logger.info("agency select clicked")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")
        
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            # data-select2-id="select2-addDeliveryType-result-e2mh-1"
            edit_button = driver.find_element(By.CLASS_NAME, "select2-search__field")
            edit_button.send_keys("Tunis branch")
            edit_button.send_keys(Keys.ENTER)
            
            
            self.logger.info("tunis office selected ")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")



    def select_delivery_address(self, driver : webdriver.Chrome):

        try:
            # click the + button
            time.sleep(3)
            element = driver.find_element(By.XPATH, '//a[@class="btn waves-effect waves-light green tooltipped modal-trigger center orderAddress"]')
            element.click()
            self.logger.info("ok + button clicked")
        except Exception as e :
            self.logger.info(f'❌Error when clicking add addrress button : {e}')

        try:
            #  select gouvernment 
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-gouvernorat_id-container").click()
            self.logger.info("select gouvernment clicked")
            time.sleep(2)
            gvr_button = driver.find_element(By.XPATH, "//li[contains(text(), 'Beja')]").click()
            self.logger.info("select Beja")
            
            
        except Exception as e :
            self.logger.info(f'❌Error when selecting gouvernment : {e}')

        try:
            #  select city
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-ville_id-container").click()
            self.logger.info("select gouvernment clicked")
            time.sleep(1)
            gvr_button = driver.find_element(By.XPATH, "//li[contains(text(), 'Beja nord')]").click()
            self.logger.info("select Beja nord")
            
        except Exception as e :
            self.logger.error(f'Error when selecting city : {e}')

        try:
            #  select locality
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-locality_id-container").click()
            self.logger.info("select locality clicked")
            time.sleep(1)
            gvr_button = driver.find_element(By.XPATH, "//li[contains(text(), 'Beja')]").click()
            self.logger.info("locality Beja ")     
        except Exception as e :
            self.logger.error(f'Error when selecting city : {e}')

        # address
        try:
            #  write address 
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "address")
            edit_button.send_keys("hay dhamen")
            
            self.logger.info("address written hay dhamen")    
        except Exception as e :
            self.logger.error(f'Error when writing address  : {e}')


        try:
            #  write phone 
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "phone1")
            edit_button.send_keys("96700480")
            self.logger.info("phone written 96700480")  
        except Exception as e :
            self.logger.error(f'Error when writing address  : {e}')

        try:
            #  save
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "addaddressAllCountry")
            edit_button.click() 
            self.logger.info("press ok")
        except Exception as e :
            self.logger.info(f'❌Error when wpressing ok  : {e}')


        try:
            # check 
            time.sleep(3)
            title = driver.find_element(By.CLASS_NAME, "swal-title")
            if title.text == "Error" : 
                self.logger.info("❌",title.text)
                text = driver.find_element(By.CLASS_NAME, "swal-text")
                self.logger.info(text.text)
            
            
        except Exception as e:
            self.logger.error(f"Error while extracting tilte : {e}")


        try:
            
            time.sleep(3)
            edit_button = driver.find_element(By.CLASS_NAME, "swal-button--confirm").click()
            
            self.logger.info("Press Ok")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on ok button : {e}")


        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-addressSelect-container").click()
            
            self.logger.info("delivery address clicked")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")
        
        try:
            
            time.sleep(3)
            
            edit_button = driver.find_element(By.CLASS_NAME, "select2-search__field")
            edit_button.send_keys("hay dhamen ,Beja,Beja nord,Beja")
            edit_button.send_keys(Keys.ENTER)                  
            self.logger.info("Address selected ")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")


    def select_payment_mode(self, driver : webdriver.Chrome):
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            edit_button = driver.find_element(By.ID, "select2-paymentMode-container").click()
            
            self.logger.info("select payment mode clicked")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on select payment mode : {e}")
        
        try:
            # Wait for the table to be visible and load completely
            time.sleep(3)
            # data-select2-id="select2-addDeliveryType-result-e2mh-1"
            edit_button = driver.find_element(By.CLASS_NAME, "select2-search__field")
            edit_button.send_keys("On delivery")
            edit_button.send_keys(Keys.ENTER)                  
            self.logger.info("carrier selected ")
            time.sleep(1)

        except Exception as e:
            self.logger.error(f"Error while clicking on edit button deposit list: {e}")

    def click_order_confirm(self, driver : webdriver.Chrome):
        try:
            driver.find_element(By.ID, "saveOrderBtn").click()
            time.sleep(2)
            
        except Exception as e:
            self.logger.error(f"Error while extracting deposit list: {e}")

    def check_if_order_confirmed_successefuly(self, driver : webdriver.Chrome):
        try:
            modal_title = driver.find_element(By.CLASS_NAME, "swal-title").text
            assert "Success" in modal_title, "Modal title is not 'Success'"
            time.sleep(2)
            self.logger.info("Result : ",modal_title)
            
        except Exception as e:
            self.logger.error(f"Error while extracting tilte : {e}")




if __name__ == "__main__":
    browser = SetupWeb()
    driver = browser.start_driver("https://qa-test:mdw@@2025@recrutement.arvea-test.ovh")
    browser.login()
    time.sleep(5)
    browser.navigate_to("https://recrutement.arvea-test.ovh/orders/create")
    page = order_page()
    page.click_load_products(driver)
    product = "ARGAN OIL SOAP"
    page.write_product_name(driver, product)
    page.add_product(driver, product)
    quantity = 5
    page.write_quantity(driver, quantity)
    page.select_head_office(driver)
    page.select_agency(driver)
    page.select_payment_mode(driver)
    page.click_order_confirm(driver)
    page.check_if_order_confirmed_successefuly(driver)
    time.sleep(5)
    # Do other stuff here...
    browser.stop_driver()