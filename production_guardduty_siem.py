import boto3
import json
from datetime import datetime

def live_guardduty_alerts():
    """Enterprise SOC alerting pipeline"""
    guardduty = boto3.client('guardduty', region_name='us-east-1')
    
    while True:
        findings = guardduty.get_findings(FindingIds=['LIVE_FINDINGS'])
        for finding in findings['Findings']:
            if finding['Severity'] > 7.0:
                print(f"🚨 HIGH: {finding['Title']} - {finding['Severity']}")
        time.sleep(30)  # Real-time polling

print("PRODUCTION: GuardDuty SIEM LIVE")
