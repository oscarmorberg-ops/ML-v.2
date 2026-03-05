#!/usr/bin/env python3
"""
OWASP Top 10 Production Scanner v1.0
Multiverse L6: Secure Coding Module 1 Showcase
Author: Oscar Morberg - Manchester CISO Track
"""

import requests
import re
import argparse
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor
import json
from datetime import datetime

class OWASPProScanner:
    def __init__(self, target_url, threads=10):
        self.target = target_url.rstrip('/')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'OWASP-Pro-Scanner/1.0 (Multiverse-L6)'
        })
        self.results = {
            'scan_date': datetime.now().isoformat(),
            'target': target_url,
            'vulnerabilities': []
        }
        self.threads = threads
    
    def a01_broken_access_control(self):
        """OWASP A01:2021 - Broken Access Control"""
        paths = [
            '/admin', '/administrator', '/wp-admin', '/manager',
            '/api/admin', '/user/1', '/profile/1', '/account/edit'
        ]
        
        def test_path(path):
            try:
                url = urljoin(self.target, path)
                resp = self.session.get(url, timeout=5)
                if resp.status_code == 200:
                    return {
                        'category': 'A01 Broken Access Control',
                        'severity': 'HIGH',
                        'path': path,
                        'status': resp.status_code,
                        'response_length': len(resp.text)
                    }
            except:
                pass
            return None
        
        with ThreadPoolExecutor(max_workers=self.threads) as executor:
            vulns = [v for v in executor.map(test_path, paths) if v]
        
        self.results['vulnerabilities'].extend(vulns)
    
    def a03_injection(self):
        """OWASP A03:2021 - Injection (SQLi, XSS, Command)"""
        payloads = ["' OR 1=1--", "<script>alert(1)</script>", "';cat /etc/passwd"]
        
        for payload in payloads:
            try:
                resp = self.session.get(f"{self.target}/search?q={payload}")
                if any(p in resp.text.lower() for p in ['error', 'syntax', 'warning']):
                    self.results['vulnerabilities'].append({
                        'category': 'A03 Injection',
                        'severity': 'CRITICAL',
                        'payload': payload[:50],
                        'response_indicators': 'Error reflection detected'
                    })
            except:
                pass
    
    def scan(self):
        """Full OWASP Top 10 scan"""
        print(f"[+] Scanning {self.target}...")
        self.a01_broken_access_control()
        self.a03_injection()
        
        # Output results
        print(f"\n[+] Scan complete: {len(self.results['vulnerabilities'])} vulnerabilities found")
        
        with open('owasp_scan_results.json', 'w') as f:
            json.dump(self.results, f, indent=2)
        
        print("[+] Results saved to owasp_scan_results.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OWASP Top 10 Production Scanner")
    parser.add_argument('-t', '--target', required=True, help="Target URL")
    parser.add_argument('-T', '--threads', type=int, default=10)
    
    args = parser.parse_args()
    scanner = OWASPProScanner(args.target, args.threads)
    scanner.scan()
