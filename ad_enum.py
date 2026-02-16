#!/usr/bin/env python3
"""
AD Enumeration Suite - Dag 050 #10/25
OSCP Active Directory attack surface mapping
CSIO+HTB pipeline → OSCP mars 100%
"""
import subprocess
import sys
import argparse

print("🔥 AD OSCP Enumeration LIVE - Dag 050 #10/25")
print("🎯 OSCP AD Attack Surface Suite")

def run_enum_commands():
    """Core OSCP AD enumeration commands"""
    commands = [
        "net user /domain",
        "net group /domain", 
        "net group 'Domain Admins' /domain",
        "net accounts /domain",
        "rpcclient -U '' TARGET_IP -c 'enumdomusers'",
        "enum4linux -a TARGET_IP"
    ]
    
    for cmd in commands:
        print(f"🏃 {cmd}")
        # subprocess.run(cmd, shell=True)  # Uncomment for live enum

def bloodhound_setup():
    """BloodHound Python collector"""
    print("🩸 BloodHound OSCP Setup:")
    print("python3 bloodhound-python -u '' -p '' -d DOMAIN -c All")
    print("python3 bloodhound-python -ns DC_IP -d DOMAIN -dc DC_HOST")

def main():
    print("🏆 OSCP AD Pipeline #10/25:")
    print("- Users: net user /domain")
    print("- Groups: net group /domain") 
    print("- RPC: rpcclient enumdomusers")
    print("- Enum4linux: full domain recon")
    print("- BloodHound: graph mapping")
    run_enum_commands()
    bloodhound_setup()
    print("✅ Dag 050 AD Enum #10 READY!")

if __name__ == "__main__":
    main()
