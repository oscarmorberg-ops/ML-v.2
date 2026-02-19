#!/usr/bin/env python3
"""
Commit #5+: GuardDuty Threat Intel Dashboard w/ GeoIP (FIXED)
"""
import boto3
import json

def analyze_threat_intel(finding):
    # Fix för olika GuardDuty finding-typer
    paths = [
        finding.get('Service', {}).get('Action', {}),
        finding.get('Service', {}).get('AwsApiCallAction', {}),
        finding.get('Service', {}).get('NetworkConnectionAction', {})
    ]
    
    for path in paths:
        if 'RemoteIpDetails' in path:
            ip_info = path['RemoteIpDetails']
            city = ip_info.get('City', {}).get('CityName', 'Unknown')
            country = ip_info.get('Country', {}).get('CountryName', 'Unknown')
            isp = ip_info.get('Organization', {}).get('Isp', 'Unknown')
            return f"📍 {country}/{city} | ISP: {isp}"
    return "✅ LOCAL/NORMAL (no external IP)"  # RootCredentialUsage = du själv!

def parse_guardduty_findings():
    gd = boto3.client('guardduty', region_name='eu-north-1')
    
    try:
        detectors = gd.list_detectors()['DetectorIds']
        if not detectors:
            print("❌ No GuardDuty detectors found")
            return
        
        print("🔍 GuardDuty Threat Analysis (eu-north-1)")
        print("=" * 60)
        
        for detector_id in detectors:
            findings = gd.list_findings(DetectorId=detector_id)['FindingIds']
            
            if findings:
                details = gd.get_findings(DetectorId=detector_id, FindingIds=findings[:5])
                
                for finding in details['Findings']:
                    print(f"🚨 {finding['Id']}")
                    print(f"   {finding['Type']} | Sev: {finding['Severity']}")
                    print(f"   👤 {analyze_threat_intel(finding)}")
                        
    except Exception as e:
        print(f"❓ GuardDuty access: {str(e)}")

if __name__ == "__main__":
    parse_guardduty_findings()

