#!/usr/bin/env python3
import subprocess

def check_windows_privesc():
    checks = [
        "net user /priv", 
        "whoami /priv",
        "systeminfo",
        "wmic service get name,pathname,startmode"
    ]
    for check in checks:
        try:
            result = subprocess.run(check, shell=True, capture_output=True, text=True)
            print(f"🔥 WIN PRIVESC: {check}")
        except:
            pass

check_windows_privesc()
