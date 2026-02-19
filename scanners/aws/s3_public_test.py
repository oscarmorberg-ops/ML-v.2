#!/usr/bin/env python3
import boto3
import requests

s3 = boto3.client('s3')
buckets = s3.list_buckets()['Buckets']

print("🌐 Testing public URLs...\n")

for bucket in buckets:
    url = f"https://{bucket['Name']}.s3.amazonaws.com/"
    try:
        r = requests.head(url, timeout=5)
        status = r.status_code
        if status == 403:
            print(f"🔒 {bucket['Name']} - Private (403)")
        elif status == 200:
            print(f"🚨 {bucket['Name']} - PUBLIC! (200)")
        else:
            print(f"❓ {bucket['Name']} - {status}")
    except:
        print(f"🔒 {bucket['Name']} - No response")

print("\n✅ Public test complete!")
