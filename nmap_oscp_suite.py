#!/usr/bin/env python3
import subprocess
import sys

def full_oscp_nmap(target):
    phases = [
        {"name": "Basic", "cmd": f"nmap -sC -sV {target}"},
        {"name": "TCP Full", "cmd": f"nmap -sS -sV -T4 -p- {target}"},
        {"name": "UDP Top", "cmd": f"nmap -sU --top-ports 100 {target}"}
    ]
    
    for phase in phases:
        print(f"🔥 {phase['name']} scan: {phase['cmd']}")
        subprocess.run(phase['cmd'], shell=True)

if __name__ == "__main__":
    full_oscp_nmap(sys.argv[1])
