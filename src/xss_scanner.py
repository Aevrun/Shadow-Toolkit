import requests
import time
import logging

logger = logging.getLogger(__name__)

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

def check_xss(url,parameter_name) -> None:
    payload = "<marquee>SHADOW_XSS</marquee>"
    separator = "&" if "?" in url else "?"
    final_url = f"{url}{separator}{parameter_name}={payload}"
    logger.info(f"[*] Sending probe to: {final_url}")
    try:
        time.sleep(0.1)
        response = requests.get(final_url,headers=headers,timeout=2)
        logger.info(f"[*] Server responded with status code: {response.status_code}") # DEBUG LINE 2
        if "SHADOW_XSS" in response.text:
            logger.info(f"[*] WARNING: parameter {final_url} is vulnerable")
    except requests.exceptions.RequestException:
        logger.error(f"[!] ERROR: Cannot connect to {url}")

