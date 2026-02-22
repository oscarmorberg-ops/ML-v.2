#!/usr/bin/env python3
import subprocess

def oscp_nmap(target):
    scans = [
        f"nmap -sC -sV -oN nmap_{target} {target}",
        f"nmap -sS -sV -T4 -oN nmap_tcp_{target} {target}",
        f"nmap -sU -sV --top-ports=100 -oN nmap_udp_{target} {target}"
    ]
    for scan in scans:
        subprocess.run(scan, shell=True)
        print(f"✅ {scan}")

oscp_nmap("10.10.10.x")
