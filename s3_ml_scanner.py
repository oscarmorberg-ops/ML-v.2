import boto3
import os

# Använd miljövariabler eller default AWS config
session = boto3.Session(
    aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
    region_name='eu-north-1'
)

s3 = session.client('s3')
print("✅ AWS Session OK - dina buckets:")
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"  📁 {bucket['Name']}")
