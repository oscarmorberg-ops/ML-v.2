#!/usr/bin/env python3
import requests, sys
from time import sleep

services = {
    's3scan': 'http://localhost:8501',
    'shscan': 'http://localhost:8503',
    'mlscan': 'http://localhost:8504', 
    'threatfusion': 'http://localhost:8508'
}

def main():
    print("🔍 CSIO Stack Health Check")
    for name, url in services.items():
        try:
            r = requests.get(f"{url}/health", timeout=5)
            print(f"✅ {name:12} {r.status_code}")
        except Exception as e:
            print(f"❌ {name:12} DOWN - {e}")
            
if __name__ == "__main__":
    main()
