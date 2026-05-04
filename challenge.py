import requests
from bs4 import BeautifulSoup

def scrape_bbc_news():
    url = "https://www.bbc.com/news"

    # Fetch the content
    # Add a user-agent string to tell the website we are a browser and not a script.
    headers = {
        "User-Agent" = "Mozilla/5.0 (Windows NT 10.0; win64; x64;) AppleWebKit/527.36 (KHTML) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        print(f"Error fetching page: {e}")
        return
    
    soup = BeautifulSoup(response.text, 'html.parser')