import boto3
import pandas as pd

def scan_simple():
    issues = []
    YOUR_ACCOUNT = "695210052227"
    
    try:
        # ALLTID funkar - S3 buckets
        s3 = boto3.client('s3')
        buckets = s3.list_buckets()['Buckets']
        
        for bucket in buckets:
            issues.append({
                'Account': YOUR_ACCOUNT,
                'Type': '✅ S3 BUCKET FOUND', 
                'Bucket': bucket['Name'],
                'Fix': 'Check public access + encryption'
            })
            
    except Exception as e:
        issues.append({'Account': YOUR_ACCOUNT, 'Error': str(e)})
    
    # Spara resultat
    df = pd.DataFrame(issues)
    df.to_csv('security-findings.csv', index=False)
    print(f"🎉 {len(issues)} S3 buckets found!")
    print(df)
    
    return issues

if __name__ == "__main__":
    scan_simple()

