import random

def calculate_risk_score(bucket_name):
    """CSIO Risk Scoring: Demo mode (0-100 poäng)"""
    score = 0
    findings = []
    
    # Demo risk logic baserat på bucket-namn
    if "public" in bucket_name or "open" in bucket_name:
        score += 50
        findings.append("A01: Public readable")
    if "unencrypted" in bucket_name or "backup" in bucket_name:
        score += 30
        findings.append("A02: Encryption missing")
    if "legacy" in bucket_name or "dev" in bucket_name:
        score += 20
        findings.append("A05: Security misconfiguration")
    
    # Random variation för realism
    score += random.randint(0, 15)
    
    risk_level = 'LOW' if score < 30 else 'MEDIUM' if score < 70 else 'HIGH'
    
    return {
        'risk_score': min(score, 100),
        'risk_level': risk_level,
        'findings': findings or ['✅ Secure configuration'],
        'color': '🟢' if score < 30 else '🟡' if score < 70 else '🔴'
    }
