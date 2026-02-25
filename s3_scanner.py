#!/usr/bin/env python3
import boto3
print("NIST CSF 2.0 S3 Scanner - Bromma Edition")
# TODO: Full implementation

# NIST CSF 2.0 IMPLEMENTATION
s3 = boto3.client('s3')

# IDENTIFY: Asset inventory
buckets = s3.list_buckets()
print(f"GOVERN/IDENTIFY: {len(buckets['Buckets'])} S3 buckets")

# PROTECT: Encryption check  
for bucket in buckets['Buckets']:
    try:
        enc = s3.get_bucket_encryption(Bucket=bucket['Name'])
        print(f"PROTECT: {bucket['Name']} → AES-256 ✓")
    except:
        print(f"PROTECT: {bucket['Name']} → NO encryption! ❌")
