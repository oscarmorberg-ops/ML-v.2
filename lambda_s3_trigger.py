import json
import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['Records'][0]['s3']['bucket']['name']
    print(f"🚨 New object in {bucket}")
