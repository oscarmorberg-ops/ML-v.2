#!/usr/bin/env python3
"""
CSIO IAM Scanner v2.0 - Dag 050
SEB IAM oversight + risky users → CSIO dashboard
"""

import boto3

def scan_iam_users():
    """CSIO IAM v2: Risky users + keys + MFA check"""
    iam = boto3.client('iam')
    
    users = iam.list_users()['Users']
    risky_users = []
    
    for user in users:
        user_name = user['UserName']
        
        # Kolla access keys
        keys = iam.list_access_keys(UserName=user_name)['AccessKeyMetadata']
        active_keys = [k for k in keys if k['Status'] == 'Active']
        
        # Kolla MFA
        mfa = iam.list_mfa_devices(UserName=user_name)
        has_mfa = len(mfa['MFADevices']) > 0
        
        risk_score = 0
        if len(active_keys) > 0: risk_score += 3
        if len(active_keys) > 2: risk_score += 2
        if not has_mfa: risk_score += 2
        
        if risk_score >= 3:
            risky_users.append({
                'user': user_name,
                'keys': len(active_keys),
                'mfa': has_mfa,
                'risk': risk_score
            })
    
    print(f"✅ CSIO IAM v2: {len(users)} users, {len(risky_users)} risky")
    for user in risky_users:
        print(f"⚠️  {user['user']}: {user['keys']} keys, MFA:{user['mfa']}")
    
    return risky_users

if __name__ == "__main__":
    print("Dag 050: CSIO IAM Scanner v2 LIVE!")
    scan_iam_users()
