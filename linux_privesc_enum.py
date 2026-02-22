#!/usr/bin/env python3
import subprocess

def check_privesc():
    checks = [
        "find / -perm -4000 2>/dev/null",
        "sudo -l 2>/dev/null", 
        "cat /etc/crontab",
        "ls -la ~/.ssh/"
    ]
    for check in checks:
        try:
            result = subprocess.run(check, shell=True, capture_output=True, text=True)
            if result.stdout or result.stderr:
                print(f"🔥 PRIVESC: {check}")
        except:
            pass

check_privesc()
