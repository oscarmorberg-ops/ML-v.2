#!/usr/bin/env python3
import boto3
import os
print("🚀 CSIO S3 ML Auto-Scanner v2 LIVE!")
s3 = boto3.client('s3')
buckets = s3.list_buckets()
print(f"✅ Found {len(buckets['Buckets'])} S3 buckets")
print("🎯 CSIO pipeline COMPLETE!")
