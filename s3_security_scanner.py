#!/usr/bin/env python3
"""
Commit #3: CSIO-grade S3 Public Access Scanner
- Checks BlockPublicAccess + Website status
"""
import boto3
import time

regions = ['eu-north-1', 'eu-central-1', 'ap-northeast-1']  # Stockholm+ top
buckets = ['oscarmorberg-portfolio-2026', 'min-cybersec-pipeline-2026']

def scan_bucket_security(s3, bucket):
    results = {}
    try:
        # Check Public Access Block
        pab = s3.get_public_access_block(Bucket=bucket)
        block_acls = pab['PublicAccessBlockConfiguration']['BlockPublicAcls']
        results['public_access'] = "🚨 PUBLIC RISK" if not block_acls else "✅ SECURE"
    except:
        results['public_access'] = "❓ UNKNOWN"
    
    try:
        # Check Website hosting (public risk)
        s3.get_bucket_website(Bucket=bucket)
        results['website'] = "🌐 PUBLIC WEBSITE"
    except:
        results['website'] = "✅ No website"
    
    return results

for region in regions:
    s3 = boto3.client('s3', region_name=region)
    print(f"🔥 {region}:")
    for bucket in buckets:
        status = scan_bucket_security(s3, bucket)
        print(f"  {bucket}: {status['public_access']} | {status['website']}")
    time.sleep(0.2)  # Rate limit
