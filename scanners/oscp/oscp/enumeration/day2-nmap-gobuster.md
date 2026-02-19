# OSCP Day 2 - Nmap + Gobuster
- nmap -sC -sV -p- -oN full_scan.txt
- gobuster dir -w /usr/share/wordlists/dirb/common.txt
- UDP top 20: nmap -sU --top-ports 20
