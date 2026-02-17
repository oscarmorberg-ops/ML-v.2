#!/usr/bin/env python3
"""
Commit #1: Real AWS Region S3 Enum
"""
import boto3

regions = ['ap-northeast-1', 'ap-northeast-3']  # Tokyo + Seoul
for region in regions:
    s3 = boto3.client('s3', region_name=region)
    print(f"\n🔥 {region}:")
    try:
        buckets = s3.list_buckets()['Buckets']
        for b in buckets:
            print(f"  {b['Name']}")
    except:
        print("  No access")
