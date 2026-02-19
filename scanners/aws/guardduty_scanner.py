<<<<<<< HEAD
def scan_guardduty_findings():
    gd = boto3.client('guardduty')
    detectors = gd.list_detectors()
    detector_id = detectors['DetectorIds']["7cce33799064eaa5d7bbbaecb6ddab3b"]  # cb6ddab3b...
    findings = gd.list_findings(DetectorId=detector_id)
    print(f"CSIO GuardDuty: {len(findings['FindingIds'])} findings")
    return findings

=======
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
>>>>>>> 99c5f50af10db3b9cb40c42d0a08841648941c9d
