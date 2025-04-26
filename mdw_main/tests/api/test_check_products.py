import time
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from requests.auth import HTTPBasicAuth

# Informations de connexion
UI_URL = "https://qa-test:mdw@@2025@recrutement.arvea-test.ovh"
LOGIN = "TN25000000"
PASSWORD = "maisonduweb123"
AUTH = HTTPBasicAuth("qa-test", "mdw@@2025")

@pytest.fixture
def selenium_login_and_get_cookies():
    """Fixture qui se connecte via Selenium et retourne les cookies de session."""
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    driver.get(UI_URL)
    time.sleep(2)
    driver.find_element(By.ID, "username").send_keys(LOGIN)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.XPATH, "//button[text()='Log In']").click()
    
    time.sleep(5)  # attendre que le tableau de bord charge
    cookies = driver.get_cookies()
    driver.quit()

    return cookies

@pytest.fixture
def create_session_with_cookies(selenium_login_and_get_cookies):
    """Crée une session requests avec les cookies récupérés depuis Selenium."""
    session = requests.Session()
    for cookie in selenium_login_and_get_cookies:
        session.cookies.set(cookie['name'], cookie['value'])
    return session

def call_get_products(session):
    """Appelle l’endpoint des produits avec les bons paramètres."""
    api_url = "https://recrutement.arvea-test.ovh/getDataProducts"
    params = {
        "page": 1,
        "per_page": 10,
        "search_product": "",
        "is_initial_load": "true",
        "advisor_id": "",
        "country_order": ""
    }

    response = session.get(api_url, params=params, auth=AUTH)
    return response

def test_get_products(create_session_with_cookies):
    """Test d’appel à l’API des produits."""
    session = create_session_with_cookies
    response = call_get_products(session)

    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    assert "products" in response.json(), "Response does not contain 'products' field"
