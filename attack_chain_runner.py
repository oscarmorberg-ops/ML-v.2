#!/usr/bin/env python3
# Full OSCP attack chain automation
steps = [
    "nmap -sC -sV 10.10.10.x",
    "./htb_sqli_scanner.py",
    "./linux_privesc_enum.py", 
    "./msf_automation.py"
]

for step in steps:
    print(f"🔥 Running: {step}")
