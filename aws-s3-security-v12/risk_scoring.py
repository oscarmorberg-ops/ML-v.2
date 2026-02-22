def calculate_risk_score(scan_results):
    """CVSS v4.0 inspired risk scoring för S3"""
    scores = {
        'critical': 0, 'high': 0, 'medium': 0, 'low': 0, 'info': 0
    }
    
    for region, buckets in scan_results.items():
        for bucket, result in buckets.items():
            if result == 'public_acl':
                scores['critical'] += 9.8
            elif result == 'policy_public':
                scores['high'] += 7.5
            elif result == 'access_denied':
                scores['info'] += 0.1
    
    return {
        'total_buckets': len([b for region_buckets in scan_results.values() 
                             for b in region_buckets]),
        'risk_vector': scores,
        'cvss_score': sum(scores.values()) / max(1, len(scan_results))
    }
