#!/usr/bin/env python3
# multiverse_cloudtrail_v2.py - Oscar Morberg Ops 2026
# Granskar AWS CloudTrail spårningsstatus i 25 regioner

import boto3
from botocore.exceptions import ClientError

REGIONS = {
    "eu-north-1": "🇸🇪 Sverige", "us-east-1": "🇺🇸 USA", 
    "af-south-1": "🇿🇦 Sydafrika", "eu-south-1": "🇮🇹 Italien",
    "ap-southeast-2": "🇦🇺 Australien", "ca-central-1": "🇨🇦 Kanada",
    "sa-east-1": "🇧🇷 Brasilien", "ap-south-1": "🇮🇳 Indien",
    "ap-northeast-1": "🇯🇵 Japan", "ap-southeast-1": "🇸🇬 Singapore",
    "eu-west-1": "🇮🇪 Irland", "eu-central-1": "🇩🇪 Tyskland", 
    "eu-west-2": "🇬🇧 UK", "eu-west-3": "🇫🇷 Frankrike",
    "us-west-2": "🇺🇸 USA West", "us-west-1": "🇺🇸 USA West-1",
    "me-south-1": "🇦🇪 UAE", "ap-northeast-2": "🇰🇷 Korea",
    "ap-northeast-3": "🇯🇵 Japan2", "eu-south-2": "🇪🇸 Spanien",
    "us-east-2": "🇺🇸 USA East2", "il-central-1": "🇮🇱 Israel",
    "ap-southeast-3": "🇮🇩 Jakarta", "ap-southeast-4": "🇦🇺 Melbourne",
    "sa-east-2": "🇧🇷 Brasilien2"
}

print("== GLOBAL CLOUDTRAIL MULTIVERSE v20 (25 regioner) ==")
print("Oscar Morberg Ops - AWS CloudTrail Granskning 2026")

clean_count = 0
protected_count = 0
protected_countries = []
no_trails_count = 0

for region, country in REGIONS.items():
    print(f"🛤️ {region} ({country}): Kontrollerar CloudTrail spårningar...")
    try:
        cloudtrail = boto3.client('cloudtrail', region_name=region)
        trails = cloudtrail.describe_trails()
        if trails['trailList']:
            print(f"   ✅ CloudTrail spårningar AKTIVA!")
            clean_count += 1
        else:
            print(f"   ⚠️  Inga CloudTrail spårningar konfigurerade")
            no_trails_count += 1
    except ClientError as e:
        error_msg = str(e)
        if any(x in error_msg for x in ["AccessDenied", "UnrecognizedClientException"]):
            print(f"   🔒 CloudTrail API otillgänglig ({country})")
            protected_countries.append(country)
            protected_count += 1
        else:
            print(f"   ❌ API-fel: {error_msg}")
    except Exception as e:
        print(f"   🔒 CloudTrail otillgänglig ({country})")
        protected_countries.append(country)
        protected_count += 1

print(f"   🏆 ANALYSRESULTAT ({len(REGIONS)} regioner):")
print(f"   ✅ Spårningar aktiva: {clean_count}")
print(f"   ⚠️  Inga spårningar: {no_trails_count}")
print(f"   🔒 API otillgänglig: {protected_count}")
if protected_countries:
    print(f"      {', '.join(protected_countries[:3])}" + (f" +{protected_count-3} till" if protected_count > 3 else ""))
print(f"   TOTAL: {len(REGIONS)}/25 regioner analyserade!")
print("GitHub: oscarmorberg-ops/cybersec-s3-pipeline")
