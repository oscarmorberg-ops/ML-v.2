from scanner import check_encryption

def calculate_risk_score(bucket_name):
    """CSIO Risk Scoring: A01+A02 kombinerat (0-100)"""
    score = 0
    findings = []
    
    # A01: Public bucket (50 poäng max)
    try:
        s3 = boto3.client('s3')
        s3.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
        score += 50
        findings.append("A01: Public readable")
    except:
        pass  # Inte publikt = bra
    
    # A02: Encryption (30 poäng)
    enc = check_encryption(bucket_name)
    if enc['a02']:
        score += 30 if enc['level'] == 'HIGH' else 15
        findings.append(f"A02: {enc.get('details', 'Encryption missing')}")
    
    # A05: Block Public Access (20 poäng)
    try:
        block = s3.get_public_access_block(Bucket=bucket_name)
        if not block['PublicAccessBlockConfiguration']['BlockPublicAcls']:
            score += 20
            findings.append("A05: Public ACLs enabled")
    except:
        score += 20
        findings.append("A05: No Block Public Access")
    
    return {
        'risk_score': min(score, 100),
        'level': 'LOW' if score < 30 else 'MEDIUM' if score < 70 else 'HIGH',
        'findings': findings,
        'color': 'green' if score < 30 else 'yellow' if score < 70 else 'red'
    }
