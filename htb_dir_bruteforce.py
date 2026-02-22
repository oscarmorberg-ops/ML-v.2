#!/usr/bin/env python3
import requests

WORDLIST = ['admin', 'login', 'wp-admin', 'phpmyadmin']
def dir_brute(target):
    for path in WORDLIST:
        resp = requests.get(f"{target}/{path}", timeout=5)
        if resp.status_code == 200:
            print(f"🔥 DIR FOUND: {path}")

dir_brute("http://10.10.10.x")
