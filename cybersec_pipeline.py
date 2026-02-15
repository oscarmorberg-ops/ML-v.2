import boto3
import json
from datetime import datetime

s3 = boto3.client('s3')
BUCKET = 'min-cybersec-pipeline-2026'

scanner_data = {
    'scan_date': '2026-01-31',
    'open_ports': [22, 80, 443],
    'vulnerabilities': ['CVE-2026-1234']
}

raw_key = f"raw/scans/2026/01/31/scan.json"
s3.put_object(Bucket=BUCKET, Key=raw_key, Body=json.dumps(scanner_data))

processed_data = {**scanner_data, 'status': 'analyzed'}
processed_key = raw_key.replace('raw', 'processed')
s3.put_object(Bucket=BUCKET, Key=processed_key, Body=json.dumps(processed_data))

print(f"Pipeline körd! Raw: {raw_key}, Processed: {processed_key}")
