#!/usr/bin/env python3
"""
OSCP Toolkit XSS Scanner (minimal example)
"""

import sys

def scan_xss(payload: str) -> str:
    print(f"[XSS] Testing payload: {payload}")
    return "OK"

def main():
    payloads = [
        '<img src=x onerror=alert(1)>',
        '<script>alert("XSS")</script>',
        '"<img src=x onerror=prompt(1)>"',
        '"><svg/onload=prompt(1)>',
    ]

    for payload in payloads:
        result = scan_xss(payload)
        if result == "OK":
            print(f"✅ Passed: {payload}")
        else:
            print(f"❌ Failed: {payload}")

if __name__ == "__main__":
    main()
