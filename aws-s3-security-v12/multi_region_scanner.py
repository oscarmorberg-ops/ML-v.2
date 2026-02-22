import boto3
from config.regions import REGIONS

def scan_all_regions(bucket_list):
    all_results = {}
    for region in REGIONS:
        print(f"🔍 {region}...")
        client = boto3.client('s3', region_name=region)
        region_results = {}
        for bucket in bucket_list:
            try:
                acl = client.get_bucket_acl(Bucket=bucket)
                region_results[bucket] = check_public_acl(acl)
            except:
                region_results[bucket] = 'access_denied'
        all_results[region] = region_results
    return all_results

def check_public_acl(acl):
    for grant in acl.get('Grants', []):
        if 'AllUsers' in grant['Grantee'].get('URI', ''):
            return True
    return False
