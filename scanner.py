def main():
    print("🚀 S3 Scanner v2.0 - 50x parallel beast mode")
    print("🔐 AWS Account: 695210052267 - Oscar's scanner")
    
    companies = ['netflix','spotify','uber','github','monzo','seb','nordea'] * 5
    bucket_names = [f"{company}-{suffix}" for company in companies 
                   for suffix in ['data','backup','public','files','prod']]
    
    print(f"🔍 Scanning {len(bucket_names)} buckets...")  # DEBUG
    
    leaks = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        results = executor.map(check_bucket, bucket_names)
        leaks = [leak for leak in results if leak]
    
    print(f"✅ {len(bucket_names)} total scanned")
    print(f"🚨 {len(leaks)} leaks found!")
    
    if leaks:
        for leak in leaks:
            print(leak)
    else:
        print("🛡️ ALL BUCKETS PRIVATE - Good security!")
    
    df = pd.DataFrame({'Leak': leaks})
    df.to_csv('s3_leaks_v2.csv', index=False)
    print("💾 s3_leaks_v2.csv ready!")
