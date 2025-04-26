import requests

# Construct the URL
url = "https://api.example.com/products"
params = {
    "product_config_id": 29,
    "stock_type": "depot",
    "depot_id": 67890
}

# Send GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    print("Success!")
    print(response.json())  # Print the response data
else:
    print(f"Failed with status code: {response.status_code}")
