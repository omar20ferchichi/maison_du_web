import json
from typing import Any, Dict
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import logging


class SetupWeb:
    user_name = "qa-test"
    user_name_password = "mdw@@2025"
    login = "TN25000000"
    login_password = "maisonduweb123"
    def __init__ (self) :
        self.logger = logging.getLogger("TestLogger")  # Using the same logger as in conftest.py
        self.logger.setLevel(logging.INFO)

    def start_driver(self, page):
        """Initialize WebDriver before each test."""
        options = Options()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.get(page)
        self.logger.info("Driver started")
        return self.driver

    def stop_driver(self):
        """Quit the WebDriver."""
        self.driver.quit()
        self.logger.info("Driver stopped")

    def login(self):
        """Perform the login process."""
        driver = self.driver

        # Fill in login form
        try:
            driver.find_element(By.ID, "username").send_keys("TN25000000")
        except Exception as e:
            self.logger.error(e)
        time.sleep(1)
        try:
            driver.find_element(By.ID, "password").send_keys("maisonduweb123")
        except Exception as e:
            self.logger.error(e)

        time.sleep(3)
        login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
        login_button.click()

        time.sleep(5)
        self.logger.info("Logged in successefuly")
    
    def navigate_to(self, page):
        try:
            
            self.driver.get(page)
            time.sleep(5) 
            self.logger.info("okNavigated to new page.")
            
        except Exception as e:
            self.logger.error(f"Error while going to new page : {e}")


if __name__ == "__main__":
    browser = SetupWeb()
    browser.start_driver("https://qa-test:mdw@@2025@recrutement.arvea-test.ovh")
    browser.login()
    
    time.sleep(5)
    # Do other stuff here...
    browser.stop_driver()