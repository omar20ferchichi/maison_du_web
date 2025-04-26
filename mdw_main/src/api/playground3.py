import time
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

def selenium_login_and_get_cookies():
    """Se connecte via Selenium et retourne les cookies de session."""
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

def create_session_with_cookies(cookies):
    """Crée une session requests et y ajoute les cookies récupérés depuis Selenium."""
    session = requests.Session()
    for cookie in cookies:
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

def main():
    print("🔐 Connexion via Selenium...")
    cookies = selenium_login_and_get_cookies()

    print("🍪 Création de session avec cookies...")
    session = create_session_with_cookies(cookies)

    print("📦 Appel à l'API des produits...")
    response = call_get_products(session)

    print("📄 Résultat de l’appel :")
    print("Status Code:", response.status_code)
    print("Response Text:\n", response.text)

if __name__ == "__main__":
    main()
