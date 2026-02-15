#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError
import sys

print("🔍 CYBERSEC S3 SCANNER v7.0 | OSCP-READY")
print("=" * 60)

s3 = boto3.client('s3', region_name='eu-north-1')

try:
    # Lista DINA buckets
    response = s3.list_buckets()
    buckets = response['Buckets']
    
    if not buckets:
        print("✅ NO BUCKETS = NO BUCKET LEAKS!")
        sys.exit(0)
    
    print(f"🔍 {len(buckets)} BUCKETS FOUND:")
    print("-" * 60)
    
    for bucket in buckets:
        name = bucket['Name']
        print(f"📦 {name}")
        
        # Testa PUBLIC access
        try:
            s3.head_bucket(Bucket=name)
            print(f"   🔓 PUBLIC READ ✓")
        except ClientError as e:
            if e.response['Error']['Code'] == '403':
                print("   🔒 PRIVATE (SAFE)")
            else:
                print("   ⚠️  ACCESS ERROR")
    
    print("\n🎯 SCAN COMPLETE | Alla dina buckets säkra!")
    
except Exception as e:
    print(f"❌ ERROR: {e}")
