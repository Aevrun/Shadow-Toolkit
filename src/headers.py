
import requests
import logging

logger = logging.getLogger(__name__)

def run_header_tester(link: str) -> None:
        try:
            logger.info(f"Beginning Header Testing for: {link}")
            response = requests.get(link)
            code  = response.status_code
            if code == 200:
                header = response.headers
                print(header.get('Server'))

                security_check = ['X-Frame-Options', 'Content-Security-Policy', 'Strict-Transport-Security']

                for each in security_check:
                    if each not in header:
                        logger.info(f"WARNING! {each} is missing in the Header")


        except requests.exceptions.RequestException:
            logger.error("[!] ERROR: could not connect to the target")

