import requests
from bs4 import BeautifulSoup
from config import HEADERS
from utils.logger import write_log

def scrape_product(url):
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        name = soup.find("h1").get_text()
        price = soup.find("p", class_="price_color").get_text()

        return name, price

    except Exception as e:
        write_log(f"Error scraping {url}: {e}")
        return None, None