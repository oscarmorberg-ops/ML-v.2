import boto3

def check_encryption(bucket_name):
    """A02: Cryptographic Failures - CSIO-nivå check"""
    s3_client = boto3.client('s3')
    
    # Bucket encryption check
    try:
        enc = s3_client.get_bucket_encryption(Bucket=bucket_name)
        algo = enc['ServerSideEncryptionConfiguration']['Rules'][0]['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']
        if algo not in ['AES256', 'aws:kms']:
            return {'a02': True, 'level': 'HIGH', 'fix': 'Enable SSE-S3/KMS'}
    except:
        return {'a02': True, 'level': 'HIGH', 'fix': 'Add default encryption'}
    
    # Object encryption sample (första 10)
    unencrypted = 0
    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=10)
        for obj in response.get('Contents', []):
            head = s3_client.head_object(Bucket=bucket_name, Key=obj['Key'])
            if 'ServerSideEncryption' not in head:
                unencrypted += 1
    except:
        pass
    
    if unencrypted > 0:
        return {'a02': True, 'level': 'MEDIUM', 'details': f'{unencrypted}/10 unencrypted'}
    
    return {'a02': False}

