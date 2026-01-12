import os.path

from src.blind_sqli import check_blind_sqli
from src.crawler import run_crawler
import logging
from src.util import get_parameters
from src.xss_scanner import check_xss
from src.sqli_scanner import check_sqli
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
wordlist = os.path.join(BASE_DIR,"wordlist.txt")
Parameter_path = os.path.join(BASE_DIR, "params.txt")

logger = logging.getLogger(__name__)

def automatic_scan(url) -> None:
    #Header scanning of the url
    logger.info("=" * 70)
    logger.info(f"Performing a header scan of the url {url}")
    #run_header_tester(url)

    # fuzzing the link
    logger.info(f"Fuzzing link: {url}")
    #run_fuzzer(url,wordlist,"env,zip")

    #Crawling the url to find links
    logger.info("=" * 70)
    logger.info(f"Crawling the url {url}")
    unique_links = set(run_crawler(url))

    #fuzzing the url to look for different paths
    with open(Parameter_path,"r") as file:
        wordlist_params = [line.strip() for line in file if line.strip()]
    for link in unique_links:
        if not link or not isinstance(link,str):
            continue
        if link.startswith(("mailto:","javascript:","#")):
            continue
        if not link.startswith("http"):
            full_target = url.rstrip("/") + "/" + link.lstrip("/")
        else:
            full_target = link
        if url in full_target:
            #fuzzing the url to fuzz parameters
            discovered_params = get_parameters(full_target)
            if discovered_params:
                for p in discovered_params:
                    logger.info(f"[!] Testing discovered parameter: {p}")
                    check_xss(full_target,p)
                    check_sqli(full_target,p)
                    check_blind_sqli(full_target,p)
                    time.sleep(0.3)
            if ".php" in full_target:
                logger.info(f"\n[*] Brute-forcing parameters from wordlist on: {full_target}")
                # We only take the top 5-10 to keep it fast, or the whole list
                for p in wordlist_params[:10]:
                    check_xss(full_target, p)
                    check_sqli(full_target, p)
                    check_blind_sqli(full_target,p)
                    time.sleep(0.3)




