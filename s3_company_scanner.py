
#!/usr/bin/env python3
"""
🔥 S3 Company Bucket Scanner v2.0 - OSCP Portfolio Tool
Scannar alla subdomains för S3 buckets och rapporterar öppna!
"""
import boto3
import requests
from datetime import datetime
import json
import time
import sys
import threading
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import urljoin

# KONFIG
THREADS = 50
TIMEOUT = 10
S3_ENDPOINTS = [
    "https://s3.amazonaws.com",
    "https://s3-eu-west-1.amazonaws.com",
    "https://s3-us-east-1.amazonaws.com"
]

def check_bucket_access(bucket_name):
    """Kolla bucket access med timeout"""
    result = {"bucket": bucket_name, "status": "error", "listable": False}
    
    for endpoint in S3_ENDPOINTS:
        try:
            url = f"{endpoint}/{bucket_name}"
            r = requests.head(url, timeout=TIMEOUT)
            
            if r.status_code == 200:
                result["status"] = "listable"
                result["listable"] = True
                return result
            elif r.status_code == 403:
                result["status"] = "private"
                return result
                
        except requests.exceptions.Timeout:
            continue
        except:
            continue
    
    return result

def generate_buckets(company):
    """Generera potentiella bucket namn"""
    prefixes = [
        f"{company.lower()}", f"{company.lower()}-assets", f"{company}-assets",
        f"{company.lower()}-uploads", f"{company}-uploads", f"{company.lower()}-files",
        f"{company}-files", f"{company.lower()}-backup", f"{company}-backup",
        f"{company.lower()}-data", f"{company}-data", f"{company.lower()}-prod",
        f"{company}-prod", f"{company.lower()}-staging", f"{company}-staging"
    ]
    return prefixes

def scan_company(company):
    """Huvudscanning"""
    print(f"🔍 Skannar {company} ({THREADS} threads)...")
    
    all_buckets = generate_buckets(company)
    publics = []
    privates = []
    
    with ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = list(executor.map(check_bucket_access, all_buckets))
    
    for r in results:
        if r["listable"]:
            publics.append(r)
        elif r["status"] == "private":
            privates.append(r)
    
    # STATISTIK
    total = len(all_buckets)
    listable_pct = (len(publics) / total * 100) if total > 0 else 0
    private_pct = (len(privates) / total * 100) if total > 0 else 0
    error_pct = 100 - listable_pct - private_pct    
    
    print(f"📊 RESULTAT {company}:")
    print(f"🚨 LISTABLE: {len(publics)} ({listable_pct:.1f}%)")
    print(f"🔒 PRIVATE: {len(privates)} ({private_pct:.1f}%)")
    print(f"⏰ TIMEOUT/ERROR: {total-len(publics)-len(privates)} ({error_pct:.1f}%)")
    print(f"TOTAL: {total} buckets")
    
    # JSON RAPPORT
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report = {
        "company": company,
        "date": timestamp,
        "total_buckets": total,
        "listable": len(publics),
        "listable_pct": round(listable_pct,1),
        "private": len(privates),
        "private_pct": round(private_pct,1),
        "error_pct": round(error_pct,1),
        "listable_buckets": [r["bucket"] for r in publics]
    }
    
    report_file = f"s3_report_{company}_{timestamp}.json"
    with open(report_file, "w") as f:
        json.dump(report, f, indent=2)
    print(f"💾 {report_file} SPARAD!")
    
    return report

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 s3_company_scanner.py <company>")
        sys.exit(1)
    
    company = sys.argv[1].upper()
    scan_company(company)
