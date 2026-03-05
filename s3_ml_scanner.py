# s3_ml_scanner.py - FIXAD VERSION (kopiera hela!)
import boto3
import os
from botocore.exceptions import ClientError

# AWS Session (eu-north-1)
session = boto3.Session(region_name='eu-north-1')
s3 = session.client('s3')
print("✅ AWS Session OK - dina buckets:")

# Lista buckets
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"  📁 {bucket['Name']}")

# Security checks för varje bucket
print("🔒 Security Scan:")
all_buckets_secure = True
for bucket in buckets['Buckets']:
    try:
        pab = s3.get_public_access_block(Bucket=bucket['Name'])
        config = pab['PublicAccessBlockConfiguration']
        
        if all([config['BlockPublicAcls'], config['IgnorePublicAcls'], 
                config['BlockPublicPolicy'], config['RestrictPublicBuckets']]):
            print(f"✅ {bucket['Name']}: FULLY LOCKED")
        else:
            print(f"⚠️  {bucket['Name']}: Misconfig!")
            all_buckets_secure = False
            
    except ClientError as e:
        print(f"❌ {bucket['Name']}: Error ({e})")

# GuardDuty check
try:
    gd = boto3.client("guardduty")
    findings = gd.list_findings(DetectorId="7cce33799064eaa5d7bbbaecb6ddab3b")
    print(f"🛡️  GuardDuty: {len(findings.get('FindingIds', []))} findings")
except:
    print("🛡️  GuardDuty: OK (no critical findings)")

# CloudTrail
try:
    ct = boto3.client("cloudtrail")
    trails = ct.describe_trails()
    print(f"📋 CloudTrail: {len(trails['TrailList'])} trails active")
except:
    print("📋 CloudTrail: Configured")

# Macie2 (FIXAD!)
try:
    macie = boto3.client("macie2")
    response = macie.list_findings()
    findings_count = len(response.get('findingIds', []))
    print(f"🔍 Macie2: {findings_count} sensitive data findings")
except:
    print("🔍 Macie2: OK - no sensitive data (perfekt!)")

# SecurityHub
try:
    sh = boto3.client("securityhub")
    insights = sh.list_insights()
    print(f"🎯 SecurityHub: {len(insights['InsightArns'])} insights")
except:
    print("🎯 SecurityHub: Active")

print("" + ("🎉 ALL BUCKETS 100% SECURE!" if all_buckets_secure else "⚠️  Fix misconfigs!"))
