import boto3

GLOBAL_REGIONS = [
    'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
    'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 
    'eu-central-1', 'eu-south-1', 'ap-southeast-1', 
    'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 
    'ap-south-1', 'ca-central-1', 'sa-east-1',
    'af-south-1'
]

def multiverse_ec2(region):
    try:
        ec2 = boto3.client('ec2', region_name=region)
        resp = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
        count = len([i for res in resp['Reservations'] for i in res['Instances']])
        return f"🌍 {region}: {count:,} EC2"
    except:
        return f"🌍 {region}: 🔒 No access"

print("=== GLOBAL EC2 MULTIVERSE v6 (18 regioner) ===")
for region in GLOBAL_REGIONS:
    print(multiverse_ec2(region))
