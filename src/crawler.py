from pathlib import Path

from bs4 import BeautifulSoup
import requests
import logging

logger = logging.getLogger(__name__)

def run_crawler(url: str) -> list:
    interesting_keywords = ["admin", "login", "upload", "config"]
    print("=" * 50)
    discovered_links = []
    logger.info("Starting crawl for URL: %s", url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            logger.info(f"Following links were scraped from the site({url}):")
            for link in links:
                href  = link.get('href')
                logger.info(f"FOUND:{href}")
                discovered_links.append(href)
                if href:
                    for each in interesting_keywords:
                        if each in href:
                            print(f"[!]IMPORTANT: {link.get('href')}")
                            logger.info(f"[!]IMPORTANT: {link.get('href')}")
                            break
    except requests.exceptions.RequestException:
        print(f"[!] ERROR: unable to connect to the url: {url}")
        logger.error(f"[!] ERROR: unable to connect to the url: {url}")
    print("=" * 50)
    return discovered_links