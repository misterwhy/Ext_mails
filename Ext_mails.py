import requests
from bs4 import BeautifulSoup
import re
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

# Define the URL of the webpage you want to scrape
url = 'https://www.example.com'

# Create a session to handle retries and headers
session = requests.Session()
retry = Retry(connect=3, backoff_factor=0.5)
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)
session.mount('https://', adapter)

# Set headers to mimic a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

try:
    # Send a GET request to the webpage with headers
    response = session.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Use a regular expression to find all email addresses in the HTML content
    emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', soup.text)

    # Remove duplicate emails if any
    emails = list(set(emails))

    # Print the extracted email addresses
    print("Found Emails:")
    for email in emails:
        print(email)

except requests.exceptions.RequestException as e:
    print(f"Error: {e}")