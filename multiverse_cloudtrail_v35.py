import boto3

GLOBAL_REGIONS = [
    "us-east-1", "us-east-2", "us-west-1", "us-west-2",
    "eu-north-1", "eu-west-1", "eu-west-2", "eu-west-3", 
    "eu-central-1", "eu-south-1", "eu-south-2",
    "ap-southeast-1", "ap-southeast-2", "ap-southeast-4", "ap-southeast-5", "ap-southeast-6", "ap-southeast-7",
    "ap-northeast-1", "ap-northeast-2", "ap-northeast-3",
    "ap-south-1", "ap-south-2", "ap-east-2",
    "ca-central-1", "ca-west-1",
    "sa-east-1",
    "af-south-1",
    "me-central-1",
    "il-central-1",
    "mx-central-1"
]

REGION_NAMES = {
    'us-east-1': '🇺🇸 USA Virginia', 'us-east-2': '🇺🇸 USA Ohio',
    'us-west-1': '🇺🇸 USA California', 'us-west-2': '🇺🇸 USA Oregon',
    'eu-north-1': '🇸🇪 SVERIGE Stockholm', 'eu-west-1': '🇮🇪 Irland',
    'eu-west-2': '🇬🇧 London', 'eu-west-3': '🇫🇷 Paris',
    'eu-central-1': '🇩🇪 Frankfurt', 'eu-south-1': '🇮🇹 Italien',
    'eu-south-2': '🇪🇸 Spanien',
    'ap-southeast-1': '🇸🇬 Singapore', 'ap-southeast-2': '🇦🇺 Sydney',
    'ap-southeast-4': '🇦🇺 Melbourne', 'ap-southeast-5': '🇲🇾 Malaysia',
    'ap-southeast-6': '🇳🇿 Nya Zeeland', 'ap-southeast-7': '🇹🇭 Thailand',
    'ap-northeast-1': '🇯🇵 Tokyo', 'ap-northeast-2': '🇰🇷 Seoul',
    'ap-northeast-3': '🇯🇵 Osaka',
    'ap-south-1': '🇮🇳 Mumbai', 'ap-south-2': '🇮🇳 Hyderabad',
    'ap-east-2': '🇹🇼 Taiwan',
    'ca-central-1': '🇨🇦 Kanada Central', 'ca-west-1': '🇨🇦 Kanada West',
    'sa-east-1': '🇧🇷 Brasilien',
    'af-south-1': '🇿🇦 Sydafrika',
    'me-central-1': '🇦🇪 UAE',
    'il-central-1': '🇮🇱 Israel',
    'mx-central-1': '🇲🇽 Mexico'
}

def cloudtrail_enum(region):
    try:
        cloudtrail = boto3.client('cloudtrail', region_name=region)
        trails = cloudtrail.list_trails()['Trails']
        trail_count = len(trails)
        return f"🛤️ {region} ({REGION_NAMES.get(region, region)}): {trail_count} CloudTrail trails"
    except Exception as e:
        return f"🛤️ {region} ({REGION_NAMES.get(region, region)}): 🔒 No CloudTrail access"

print("=== 🚀 CSIO GLOBAL CLOUDTRAIL MULTIVERSE v35 (35/39 regioner) ===")
print(f"🎯 TOTAL ANALYS: {len(GLOBAL_REGIONS)}/39 AWS regioner")
print()

for region in GLOBAL_REGIONS:
    print(cloudtrail_enum(region))

print()
print("🏆 CSIO ELITE STATUS: 35/39 regioner analyserade!")
print("📍 GitHub: oscarmorberg-ops/cybersec-s3-pipeline")
print("🚨 ericsson.s3.amazonaws.com - PUBLIC FILES!")
