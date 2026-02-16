#!/usr/bin/env python3
"""
Linux Privesc Framework - Dag 050 #12/25
OSCP Linux privilege escalation enumeration
"""
print("🔥 LINUX PRIVESC OSCP LIVE - Dag 050 #12!")
print("🎯 LinPEAS + manual enum pipeline:")

privesc_checks = [
    "sudo -l",
    "sudo find / -perm -u=s -type f 2>/dev/null",
    "find / -writable -type d 2>/dev/null",
    "vi /etc/passwd",
    "uname -a; cat /etc/*release",
    "./linpeas.sh"
]

for check in privesc_checks:
    print(f"🏃 {check}")

print("✅ Dag 050 Linux Privesc #12 READY!")
