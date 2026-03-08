import boto3
import os
#from slack_sdk import WebhookClient
#from dotenv import load_dotenv

## load_dotenv()

def scan_iam_policies():
    # 🧪 MOCK MODE för Multiverse demo
    mock_vulns = [
        "arn:aws:iam::123456789012:policy/PublicReadAccess", 
        "arn:aws:iam::987654321098:policy/EveryoneCanLogin"
    ]
    print("🔍 s3scan v3 MOCK: 2 IAM vulns för live demo")
    return mock_vulns

vulns = scan_iam_policies()
print(f"🚨 Found {len(vulns)} IAM vulns: {vulns}")
