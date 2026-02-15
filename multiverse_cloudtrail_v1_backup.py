import boto3

GLOBAL_REGIONS = [
    'us-east-1', 'us-east-2', 'us-west-1', 'us-west-2',
    'eu-north-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 
    'eu-central-1', 'eu-south-1', 'ap-southeast-1', 
    'ap-southeast-2', 'ap-northeast-1', 'ap-northeast-2', 
    'ap-south-1', 'ca-central-1', 'sa-east-1', 'af-south-1'
]

REGION_NAMES = {
    'us-east-1': '🇺🇸 USA Virginia', 'us-east-2': '🇺🇸 USA Ohio',
    'us-west-1': '🇺🇸 USA California', 'us-west-2': '🇺🇸 USA Oregon',
    'eu-north-1': '🇸🇪 SVERIGE', 'eu-west-1': '🇮🇪 Irland',
    'eu-west-2': '🇬🇧 London', 'eu-west-3': '🇫🇷 Paris',
    'eu-central-1': '🇩🇪 Tyskland', 'eu-south-1': '🇮🇹 Italien',
    'ap-southeast-1': '🇸🇬 Singapore', 'ap-southeast-2': '🇦🇺 Australien',
    'ap-northeast-1': '🇯🇵 Japan', 'ap-northeast-2': '🇰🇷 Korea',
    'ap-south-1': '🇮🇳 Indien', 'ca-central-1': '🇨🇦 Kanada',
    'sa-east-1': '🇧🇷 Brasilien', 'af-south-1': '🇿🇦 Sydafrika'
}

def cloudtrail_enum(region):
    try:
        cloudtrail = boto3.client('cloudtrail', region_name=region)
        trails = cloudtrail.list_trails()['Trails']
        trail_count = len(trails)
        return f"🛤️ {region} ({REGION_NAMES[region]}): {trail_count} CloudTrail trails"
    except:
        return f"🛤️ {region} ({REGION_NAMES[region]}): 🔒 No CloudTrail access"

print("=== GLOBAL CLOUDTRAIL MULTIVERSE v20 (18 regioner) ===")
for region in GLOBAL_REGIONS:
    print(cloudtrail_enum(region))
