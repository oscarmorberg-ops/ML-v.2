#!/usr/bin/env python3
"""
Commit #2: Real AWS Region S3 Enum - Enabled Regions
"""
import boto3

# Alla AWS S3 "Enabled by default" regioner från din lista
regions = [
    'ap-northeast-1',  # Tokyo ✓
    'ap-northeast-2',  # Seoul ✓ 
    'ap-northeast-3',  # Osaka ✓
    'ap-south-1',      # Mumbai
    'ap-southeast-1',  # Singapore
    'ap-southeast-2',  # Sydney
    'ca-central-1',    # Canada Central
    'eu-central-1',    # Frankfurt
    'eu-north-1',      # Stockholm ← HEMMA!
    'eu-west-1',       # Ireland
    'eu-west-2',       # London
    'eu-west-3',       # Paris
    'sa-east-1'        # São Paulo
]

for region in regions:
    s3 = boto3.client('s3', region_name=region)
    print(f"🔥 {region}:")
    try:
        buckets = s3.list_buckets()['Buckets']
        for b in buckets:
            print(f"  {b['Name']}")
    except:
        print("  No access")
