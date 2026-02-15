#!/usr/bin/env python3
import requests

# Vanliga svenska företag + patterns
targets = [
    "seb-se", "seb-bank", "seb-prod", "seb-uploads",
    "handelsbanken-se", "handelsbanken", "swedbank-se", 
    "nordea-se", "nordea", "volvo-se", "volvo-cars",
    "ericsson-se", "ericsson", "scania-se", "ikea-se"
]

print("🎯 S3 BUCKET HUNTER - External scan\n")

for base in targets:
    buckets = [
        f"{base}.s3.amazonaws.com",
        f"{base}-uploads.s3.amazonaws.com",
        f"{base}-prod.s3.amazonaws.com",
        f"{base}-backup.s3.amazonaws.com",
        f"{base}-assets.s3.amazonaws.com"
    ]
    
    for bucket in buckets:
        try:
            r = requests.head(f"https://{bucket}", timeout=3)
            if r.status_code == 403:
                print(f"🔒 {bucket} - Private")
            elif r.status_code == 200:
                print(f"🚨🚨 {bucket} - PUBLIC FILES! 🚨🚨")
            else:
                print(f"⚪ {bucket} - {r.status_code}")
        except:
            print(f"⚪ {bucket} - No DNS")
