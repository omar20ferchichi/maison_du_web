import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from requests.auth import HTTPBasicAuth

# --- Step 1: Selenium login ---
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# Open the website (do not include basic auth in URL here)
driver.get("https://qa-test:mdw@@2025@recrutement.arvea-test.ovh")

# Login form
time.sleep(2)
driver.find_element(By.ID, "username").send_keys("TN25000000")
driver.find_element(By.ID, "password").send_keys("maisonduweb123")
login_button = driver.find_element(By.XPATH, "//button[text()='Log In']")
login_button.click()

# Wait for dashboard to load
time.sleep(5)

# --- Step 2: Get cookies from Selenium session ---
cookies = driver.get_cookies()
driver.quit()

# --- Step 3: Use requests to call the API ---
session = requests.Session()

# Transfer cookies from Selenium to requests
for cookie in cookies:
    session.cookies.set(cookie['name'], cookie['value'])

# Add HTTP Basic Auth
auth = HTTPBasicAuth("qa-test", "mdw@@2025")

# API URL
api_url = "https://recrutement.arvea-test.ovh/getDataProducts?page=1&per_page=10&search_product=&is_initial_load=true&advisor_id=&country_order="

# Make the API request
response = session.get(api_url, auth=auth)

# --- Step 4: Show result ---
print("Status Code:", response.status_code)
print("Response Text:\n", response.text)
print("_______________________________________________")
print("_______________________________________________")
print("_______________________________________________")
print("_______________________________________________")
print(response.json())
filename="response_output.json"
with open(filename, "w", encoding="utf-8") as f:
    f.write(str(response.json()))
