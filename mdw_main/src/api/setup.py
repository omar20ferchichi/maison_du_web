import requests
from requests.auth import HTTPBasicAuth

# Base URL for authentication and data retrieval
base_url = "https://qa-test:mdw@@2025@recrutement.arvea-test.ovh"

# Login credentials
login_url = f"{base_url}/login"  # Adjust according to the actual login endpoint
login_data = {
    'login': "TN25000000",
    'password': "maisonduweb123"
}

# Data for fetching products
data_products_url = f"{base_url}/getDataProducts"
params = {
    "page": 1,
    "per_page": 10,
    "search_product": "bb",  # Example search term
    "is_initial_load": "false",
    "advisor_id": "",
    "country_order": ""
}

# Start a session to maintain cookies and headers
session = requests.Session()

# Perform the initial authentication
try:
    response = session.get(base_url)
    if response.status_code == 200:
        print("Successfully connected with embedded credentials.")
    else:
        print(f"Failed to connect with embedded credentials. Status code: {response.status_code}")
        # Proceed with manual login
except Exception as e:
    print(f"Error during connection: {e}")

# Perform manual login if embedded credentials didn't work
if response.status_code != 200:
    login_response = session.post(login_url, data=login_data)
    if login_response.status_code == 200:
        print("Login successful!")
    else:
        print(f"Login failed. Status code: {login_response.status_code}")

# Step 3: Fetch product data
response = session.get(data_products_url, params=params, auth=HTTPBasicAuth("qa-test", "mdw@@2025"))

# Check if the response is successful
if response.status_code == 200:
    try:
        # Try to parse JSON response
        data = response
        print( data.json())
    except ValueError:
        print(f"Error parsing JSON. Raw response: {response.text}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}. Response: {response.text}")
