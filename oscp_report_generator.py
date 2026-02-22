#!/usr/bin/env python3
# Production OSCP report generator
template = """
# OSCP Exam Report
## Target: 10.10.10.x
### 1. Nmap
### 2. Web Vulns (SQLi/XSS)
### 3. Privesc Linux/Windows
### 4. Root flag: 

**Timeline:** 2h30min
"""

print(template)
