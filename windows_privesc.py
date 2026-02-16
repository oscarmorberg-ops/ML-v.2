#!/usr/bin/env python3
"""
Windows Privesc Framework - Dag 050 #13/25
OSCP Windows privilege escalation
"""
print("🔥 WINDOWS PRIVESC OSCP - Dag 050 #13/25")
print("🎯 WinPEAS + Manual Privesc Pipeline")

win_checks = [
    "whoami /all",                    # Token privileges
    "net user administrator",         # Admin status  
    "systeminfo | findstr /B /C:\"OS Name\" /C:\"OS Version\"",
    "wmic qfe list full | findstr KB", # Hotfixes
    "net localgroup administrators",  # Local admins
    "type C:\Windows\Panther\setupact.log", # UAC bypass
    "./winpeas.exe quiet"             # Auto enum
]

for check in win_checks:
    print(f"🏃 {check}")

print("✅ Dag 050 Windows Privesc #13 READY!")
