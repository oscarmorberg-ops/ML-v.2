#!/usr/bin/env python3
"""
CSIO GuardDuty Scanner v1.0 - Dag 050
AWS GuardDuty findings → CSIO dashboard
"""

import boto3
import json
from datetime import datetime

def scan_guardduty_findings():
    """Scan GuardDuty findings för CSIO oversight"""
    gd = boto3.client('guardduty')
    
    findings = gd.list_findings(DetectorId='7cce33799064eaa5d7bbbaecb6ddab3b')
    print(f"CSIO GuardDuty: {len(findings['FindingIds'])} findings")
    
    return findings

if __name__ == "__main__":
    print("Dag 050: CSIO GuardDuty scanner LIVE!")
    scan_guardduty_findings()
