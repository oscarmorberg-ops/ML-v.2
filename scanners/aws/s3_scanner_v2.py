<<<<<<< HEAD
def generate_top_buckets(company):
    """v3.0 - 12 smart buckets istället för 100+ dubbletter"""
    base = company.lower().replace(' ', '-')
    return [
        f"{base}.s3.amazonaws.com",
        f"{base}-data.s3.amazonaws.com",
        f"{base}-prod.s3.amazonaws.com",
        f"{base}-uploads.s3.amazonaws.com",
        f"{base}-static.s3.amazonaws.com",
        f"{base}-media.s3.amazonaws.com",
        f"{base}-logs.s3.amazonaws.com",
        f"{base}-backup.s3.amazonaws.com",
        f"{base}-assets.s3.amazonaws.com",
        f"{base}-public.s3.amazonaws.com",
        f"{base}-files.s3.amazonaws.com",
        f"{base}-content.s3.amazonaws.com"
    ]

def main():
    print("🚀 S3 Scanner v3.0 - Smart 12-bucket scan")
    
    company = "Klarna"  # eller args.company
    
    # NY v3.0: Bara 12 smarta buckets!
    bucket_names = generate_top_buckets(company)
    print(f"🔍 {len(bucket_names)} smart buckets för {company}")
=======
import boto3
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

# Din Netflix-pwning lista
companies = ['netflix','spotify','uber','github','monzo','seb','nordea'] * 5

def check_bucket(bucket_name):
    """Parallel bucket check - 50x snabbare än v1"""
    try:
        s3 = boto3.client('s3')
        s3.head_bucket(Bucket=bucket_name)
        return f"🚨 LEAK: {bucket_name}"
    except:
        return None

def main():
    print("🚀 S3 Scanner v2.0 - 50x parallel beast mode")
    
    # Generate bucket names
    bucket_names = [f"{company}-{suffix}" for company in companies 
                   for suffix in ['data','backup','public','files','prod']]
>>>>>>> e9b292cc5d88189fe4aabaa7ab8cfe876ca0bc53
    
    leaks = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(check_bucket, bucket_names)
<<<<<<< HEAD
        leaks = [r for r in results if r]
=======
        leaks = [leak for leak in results if leak]
    
    print(f"✅ {len(leaks)} leaks found!")
    for leak in leaks:
        print(leak)
    
    # CSV för portfolio
    df = pd.DataFrame({'Leak': leaks})
    df.to_csv('s3_leaks_v2.csv', index=False)
    print("💾 s3_leaks_v2.csv ready!")

if __name__ == "__main__":
    main()
>>>>>>> e9b292cc5d88189fe4aabaa7ab8cfe876ca0bc53
