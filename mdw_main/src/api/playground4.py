import requests
from bs4 import BeautifulSoup

# URL of the API or webpage
url = 'https://example.com/api_page'

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract data from the page (for example, find all paragraphs)
    data = soup.find_all('p')  # You can adjust this to target the specific data you need
    
    for item in data:
        print(item.text)  # This will print the text of each <p> tag
else:
    print(f"Failed to retrieve the page, status code: {response.status_code}")
