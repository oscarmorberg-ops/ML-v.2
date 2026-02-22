import boto3
from config.regions import REGIONS
from botocore.exceptions import ClientError

class S3MultiRegionClient:
    def __init__(self):
        self.clients = {region: boto3.client('s3', region_name=region) 
                       for region in REGIONS}
    
    def get_bucket_region(self, bucket):
        """Auto-detect bucket region"""
        for region, client in self.clients.items():
            try:
                client.head_bucket(Bucket=bucket)
                return region
            except ClientError as e:
                if '301' in str(e):
                    location = e.response['Error']['Region']
                    return location
        return None
    
    def scan_bucket(self, bucket):
        region = self.get_bucket_region(bucket)
        if region:
            return self.clients[region].get_bucket_acl(Bucket=bucket)
        return None
