#!/usr/bin/env python3
"""
CSIO CloudTrail v5 Scanner - Dag 050
CloudTrail logs → CSIO oversight dashboard
"""

import boto3
from datetime import datetime, timedelta

def scan_cloudtrail_events():
    """Scan CloudTrail events för CSIO oversight"""
    ct = boto3.client('cloudtrail')
    
    # Senaste 7 dagars events
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)
    
    try:
        response = ct.lookup_events(
            LookupAttributes=[
                {
                    'AttributeKey': 'EventSource',
                    'AttributeValue': 's3.amazonaws.com'
                }
            ],
            StartTime=start_time,
            EndTime=end_time
        )
        
        events = len(response['Events'])
        print(f"✅ CSIO CloudTrail v5: {events} S3 events (7d)")
        
        # Risky events
        risky = [e for e in response['Events'] 
                if 'DeleteBucket' in e.get('EventName', '') or 
                   'PutBucketPolicy' in e.get('EventName', '')]
        
        print(f"⚠️  CSIO Alerts: {len(risky)} risky S3 events")
        return response
        
    except Exception as e:
        print(f"❌ CSIO CloudTrail error: {e}")
        return []

if __name__ == "__main__":
    print("Dag 050: CSIO CloudTrail v5 LIVE!")
    scan_cloudtrail_events()
