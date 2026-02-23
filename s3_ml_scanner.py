import os
import boto3
from botocore.exceptions import NoCredentialsError

try:
    s3 = boto3.client(
        's3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
        region_name=os.getenv('AWS_DEFAULT_REGION', 'eu-north-1')
    )
    buckets = s3.list_buckets()['Buckets']
    print(f"✅ Found {len(buckets)} S3 buckets!")
except NoCredentialsError:
    print("❌ AWS credentials saknas. Kör 'aws configure' eller sätt miljövariabler.")
except Exception as e:
    print(f"🚨 Fel: {e}")
