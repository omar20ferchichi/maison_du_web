import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from requests.auth import HTTPBasicAuth

# 🔐 Login & API configuration
UI_URL = "https://qa-test:mdw@@2025@recrutement.arvea-test.ovh"
LOGIN = "TN25000000"
PASSWORD = "maisonduweb123"
AUTH = HTTPBasicAuth("qa-test", "mdw@@2025")

# The target URL you want to interact with
API_URL = "https://recrutement.arvea-test.ovh/orders?draw=1&columns%5B0%5D%5Bdata%5D=id&columns%5B0%5D%5Bname%5D=id&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=timezone&columns%5B1%5D%5Bname%5D=timezone&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=created_at&columns%5B2%5D%5Bname%5D=created_at&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=validation_date&columns%5B3%5D%5Bname%5D=validation_date&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=false&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=date_masking&columns%5B4%5D%5Bname%5D=date_masking&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=false&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=typeCommande&columns%5B5%5D%5Bname%5D=typeCommande&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=false&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=net_pay&columns%5B6%5D%5Bname%5D=net_pay&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=false&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=ac&columns%5B7%5D%5Bname%5D=ac&columns%5B7%5D%5Bsearchable%5D=true&columns%5B7%5D%5Borderable%5D=false&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=transporter.name&columns%5B8%5D%5Bname%5D=transporter.name&columns%5B8%5D%5Bsearchable%5D=false&columns%5B8%5D%5Borderable%5D=false&columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B9%5D%5Bdata%5D=depot.name&columns%5B9%5D%5Bname%5D=depot.name&columns%5B9%5D%5Bsearchable%5D=false&columns%5B9%5D%5Borderable%5D=false&columns%5B9%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B9%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B10%5D%5Bdata%5D=etat&columns%5B10%5D%5Bname%5D=etat&columns%5B10%5D%5Bsearchable%5D=true&columns%5B10%5D%5Borderable%5D=false&columns%5B10%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B10%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B11%5D%5Bdata%5D=paymentmode.name&columns%5B11%5D%5Bname%5D=paymentmode.name&columns%5B11%5D%5Bsearchable%5D=false&columns%5B11%5D%5Borderable%5D=false&columns%5B11%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B11%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B12%5D%5Bdata%5D=paid&columns%5B12%5D%5Bname%5D=paid&columns%5B12%5D%5Bsearchable%5D=false&columns%5B12%5D%5Borderable%5D=false&columns%5B12%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B12%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B13%5D%5Bdata%5D=bordereau&columns%5B13%5D%5Bname%5D=bordereau&columns%5B13%5D%5Bsearchable%5D=true&columns%5B13%5D%5Borderable%5D=false&columns%5B13%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B13%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B14%5D%5Bdata%5D=action&columns%5B14%5D%5Bname%5D=action&columns%5B14%5D%5Bsearchable%5D=false&columns%5B14%5D%5Borderable%5D=false&columns%5B14%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B14%5D%5Bsearch%5D%5Bregex%5D=false&start=0&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&_=1745607191848"

def selenium_login_and_get_cookies():
    """Login via Selenium and return cookies for the session."""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get(UI_URL)
    time.sleep(2)

    driver.find_element(By.ID, "username").send_keys(LOGIN)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Log In']").click()

    time.sleep(5)  # Wait for login to complete
    cookies = driver.get_cookies()
    driver.quit()

    return cookies

def create_session_with_cookies(cookies):
    """Create a requests session and add Selenium cookies."""
    session = requests.Session()
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session

def fetch_orders(session : requests.Session):
    """Fetch orders data."""
    response = session.get(API_URL, auth=AUTH)
    if response.status_code == 200:
        try:
            data = response.json()
            print("📦 Orders data:", data)
            filename="response_output.json"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(str(data))
        except Exception as e :
            print(e)
    else:
        print("❌ Error fetching orders:", response.status_code)
        print(response.text)

def main():
    print("🔐 Logging in via Selenium...")
    cookies = selenium_login_and_get_cookies()

    print("🍪 Creating session with cookies...")
    session = create_session_with_cookies(cookies)

    print("📝 Fetching orders data...")
    fetch_orders(session)

if __name__ == "__main__":
    main()
