'''Basic Web Scraper
Description: A program that extracts data from a given website and displays the information in a readable format'''

import requests
from bs4 import BeautifulSoup

def basic_web_scraper(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Example: Extract all the links from the page
        links = soup.find_all('a')
        
        # Print all the links
        for link in links:
            print(link.get('href'))
    else:
        print(f"Failed to retrieve content, status code {response.status_code}")


if __name__ == "__main__":
    # URL of the webpage to scrape
    url = input("enter the url:")
    basic_web_scraper(url) 
