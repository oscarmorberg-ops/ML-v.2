import boto3
from config.regions import REGIONS

def scan_all_regions(bucket_list):
    """Scan S3 buckets across EU/US regions"""
    all_results = {}
    
    for region in REGIONS:
        print(f"🔍 Scanning {region}...")
        client = boto3.client('s3', region_name=region)
        
        region_results = {}
        for bucket in bucket_list:
            try:
                acl = client.get_bucket_acl(Bucket=bucket)
                policy = client.get_bucket_policy_status(Bucket=bucket)
                region_results[bucket] = {
                    'public_acl': check_public_acl(acl),
                    'policy_status': policy['PolicyStatus']['IsPublic']
                }
            except:
                region_results[bucket] = 'access_denied'
        
        all_results[region] = region_results
    
    return all_results

def check_public_acl(acl):
    for grant in acl.get('Grants', []):
        if grant['Grantee'].get('Type') == 'Group' and 'AllUsers' in grant['Grantee'].get('URI', ''):
            return True
    return False
