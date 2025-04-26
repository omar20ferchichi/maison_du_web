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

ORDERS_API_URL = "https://recrutement.arvea-test.ovh/orders"

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

def call_orders(session):
    """Appelle l’endpoint des commandes avec tous les paramètres."""
    params = {
        "draw": 1,
        "start": 0,
        "length": 10,
        "search[value]": "",
        "search[regex]": "false",
    }

    # Ajouter les colonnes à la requête (simplification, pas toutes les colonnes ici pour la lisibilité)
    columns = [
        "id", "timezone", "created_at", "validation_date", "date_masking",
        "typeCommande", "net_pay", "ac", "transporter.name", "depot.name",
        "etat", "paymentmode.name", "paid", "bordereau", "action"
    ]
    for i, col in enumerate(columns):
        params[f"columns[{i}][data]"] = col
        params[f"columns[{i}][name]"] = col
        params[f"columns[{i}][searchable]"] = "true" if "name" not in col and "action" not in col else "false"
        params[f"columns[{i}][orderable]"] = "false"
        params[f"columns[{i}][search][value]"] = ""
        params[f"columns[{i}][search][regex]"] = "false"

    response = session.get(ORDERS_API_URL, params=params, auth=AUTH)
    return response

def main():
    print("🔐 Connexion via Selenium...")
    cookies = selenium_login_and_get_cookies()

    print("🍪 Création de session avec cookies...")
    session = create_session_with_cookies(cookies)

    print("📦 Appel à l'API des commandes...")
    response = call_orders(session)

    print("📄 Résultat de l’appel :")
    print("Status Code:", response.status_code)
    print("Response JSON:")
    print(response.json())

if __name__ == "__main__":
    main()
