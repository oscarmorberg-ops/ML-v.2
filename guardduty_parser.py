#!/usr/bin/env python3
"""
Commit #5: GuardDuty JSON Parser + Threat Intel Extractor
Parse oscar-guardduty-findings för CSIO dashboard
"""
import boto3
import json

def parse_guardduty_findings():
    gd = boto3.client('guardduty', region_name='eu-north-1')
    
    try:
        # Lista detectors och findings
        detectors = gd.list_detectors()['DetectorIds']
        if not detectors:
            print("❌ No GuardDuty detectors found")
            return
        
        print("🔍 GuardDuty Threat Analysis (eu-north-1)")
        print("=" * 50)
        
        for detector_id in detectors:
            findings = gd.list_findings(DetectorId=detector_id)['FindingIds']
            
            if findings:
                details = gd.get_findings(DetectorId=detector_id, FindingIds=findings[:5])  # Top 5
                
                for finding in details['Findings']:
                    print(f"🚨 FINDING: {finding['Id']}")
                    print(f"   Severity: {finding['Severity']}")
                    print(f"   Type: {finding['Type']}")
                    print(f"   Created: {finding['CreatedAt']}")
                    
                    # Extrahera hot-IPs och threats
                    if 'Resource' in finding and 'InstanceDetails' in finding['Resource']:
                        print(f"   Instance: {finding['Resource']['InstanceDetails']['InstanceId']}")
                    
                    if 'Service' in finding and 'Action' in finding['Service']:
                        print(f"   Action: {finding['Service']['Action']}")
                        
    except Exception as e:
        print(f"❓ GuardDuty access: {str(e)}")

if __name__ == "__main__":
    parse_guardduty_findings()
