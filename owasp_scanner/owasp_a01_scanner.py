#!/usr/bin/env python3
"""OWASP Top 10 A01: Broken Access Control Scanner - Multiverse L6"""

import requests
from urllib.parse import urljoin, urlparse

class OWASPA01Scanner:
    def __init__(self, target_url):
        self.target = target_url
        self.session = requests.Session()
    
    def test_idor(self, base_path):
        """Test Insecure Direct Object References"""
        paths = ['/admin', '/user/1', '/api/private', '/config']
        results = []
        for path in paths:
            test_url = urljoin(self.target, base_path + path)
            resp = self.session.get(test_url)
            if resp.status_code == 200:
                results.append(f"VULN: IDOR detected {test_url}")
        return results

# Multiverse L6 demo
scanner = OWASPA01Scanner("http://testsite.com")
print(scanner.test_idor("/"))
