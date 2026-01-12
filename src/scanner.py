import socket
import logging

logger = logging.getLogger(__name__)

def run_scanner(target,strt,final) -> None:
    # simple port scanner to check for open ports on the local host
    print("=" * 50)
    logger.info(f"Starting port scanning on {target} range({strt,final})")
    for port in range(strt,final + 1):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(0.01)
        try:
            result = sock.connect_ex((target,port))
            if result == 0:
                logger.info(f"SCANNER: Port {port} is open")
            sock.close()
        except socket.error as e:
            logger.error(f"could not connect to {target}: {e}")
    print("=" * 50)
    logger.info(f"Port Scanning for {target} done")