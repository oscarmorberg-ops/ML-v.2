import boto3

GLOBAL_REGIONS = [  # Dina 18 regioner
    'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
    'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 
    'eu-central-1', 'eu-south-1', 'ap-southeast-1', 
    'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 
    'ap-south-1', 'ca-central-1', 'sa-east-1', 'af-south-1'
]

def iam_enum(region):
    try:
        iam = boto3.client('iam', region_name=region)
        users = iam.list_users()['Users']
        user_count = len(users)
        return f"🔑 {region}: {user_count} IAM users"
    except:
        return f"🔑 {region}: 🔒 No IAM access"

print("=== GLOBAL IAM MULTIVERSE v19 (18 regioner) ===")
for region in GLOBAL_REGIONS:
    print(iam_enum(region))
