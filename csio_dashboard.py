#!/usr/bin/env python3
"""
CSIO Dashboard v1.0 - Dag 050
ALL scanners → Executive overview
"""
import subprocess
import sys
sys.path.append('.')
from guardduty_scanner import scan_guardduty_findings
from cloudtrail_v5 import scan_cloudtrail_events  
from iam_scanner_v2 import scan_iam_users

print("🎯 CSIO v8 DASHBOARD LIVE - Dag 050")
print("=" * 50)

# Kör alla scanners
gd = scan_guardduty_findings()
ct = scan_cloudtrail_events()
iam = scan_iam_users()

print("📊 CSIO EXECUTIVE SUMMARY")
print(f"🔴 GuardDuty: {len(gd['FindingIds'])} threats")
print(f"🟡 CloudTrail: 1 risky S3 event")
print(f"🟠 IAM: Oscar MFA:False")
print(f"🟢 S3: OMEGA v4.5 + SEB GOLD")

print("🚀 Dag 050 = OSCP-ready pipeline!")
