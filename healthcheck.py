import requests
from time import sleep

services = {
    's3scan': 'http://localhost:8501',
    'shscan': 'http://localhost:8503', 
    'mlscan': 'http://localhost:8504',
    'threatfusion': 'http://localhost:8508'
}

def check_csio_stack():
    for name, url in services.items():
        try:
            r = requests.get(url + '/health', timeout=5)
            print(f"✅ {name}: {r.status_code}")
        except:
            print(f"❌ {name}: DOWN")
