#!/usr/bin/env python3
import socket
from concurrent.futures import ThreadPoolExecutor

def check_ssh_open(ip):
    sock = socket.socket()
    sock.settimeout(1)
    result = sock.connect_ex((ip, 22))
    sock.close()
    return "SSH ÖPPEN" if result == 0 else "stängd"

# Testa direkt:
print(check_ssh_open("16.170.248.238"))
REGIONS = ['eu-north-1', 'eu-west-1', 'eu-central-1', 'us-east-1']

print("=== CYBERSEC MULTIVERSE v1 ===")
for region in REGIONS:
    print(f"🔍 Skannar {region} för SSH...")
