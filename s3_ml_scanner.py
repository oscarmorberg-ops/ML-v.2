import boto3
import os

# Använd miljövariabler eller default AWS config
session = boto3.Session(
    region_name='eu-north-1'
)

s3 = session.client('s3')
print("✅ AWS Session OK - dina buckets:")
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print(f"  📁 {bucket['Name']}")
def risk_score(bucket):
    score = random.uniform(1, 10)
    return f"🔴 {score:.1f}/10"
