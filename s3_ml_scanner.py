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
gd = boto3.client("guardduty")
findings = gd.list_findings(DetectorId="7cce33799064eaa5d7bbbaecb6ddab3b")
for bucket in buckets["Buckets"]:
    pab = s3.get_public_access_block(Bucket=bucket["Name"])
    print(f"  🔒 {bucket['Name']}: {pab}")
ct = boto3.client("cloudtrail")
trails = ct.describe_trails()
macie = boto3.client("macie2")
classifiers = macie.list_classifiers()
