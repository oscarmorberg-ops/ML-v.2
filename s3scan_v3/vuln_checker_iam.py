import json
import re

class VulnCheckerIAM:
    def __init__(self):
        self.critical_patterns = [
            r"\"Effect\":\"Allow\".*\"Principal\":\"\*\"",
            r"\"Action\":\"s3:GetObject\".*\"Principal\":\"\*\"",
            r"PublicRead",
            r"EveryoneCanRead"
        ]
    
    def check_policy_vulns(self, policy_json):
        """Analyserar IAM policy för kritiska vulns"""
        vulns = []
        try:
            policy = json.loads(policy_json)
            statements = policy.get('Statement', [])
            
            for stmt in statements:
                if stmt.get('Effect') == 'Allow':
                    principal = stmt.get('Principal', {})
                    action = stmt.get('Action', [])
                    
                    # Public access vuln
                    if principal == '*' or 'AWS' in str(principal) and '*' in str(principal):
                        vulns.append("CRITICAL: Public Principal *")
                    
                    # S3 public read
                    if 's3:GetObject' in str(action) and principal == '*':
                        vulns.append("HIGH: Public S3 read access")
                        
        except json.JSONDecodeError:
            vulns.append("ERROR: Invalid JSON policy")
        
        return vulns
    
    def severity_score(self, vulns):
        scores = {'CRITICAL': 10, 'HIGH': 7, 'MEDIUM': 4}
        return sum(scores.get(v.split(':')[0], 1) for v in vulns)

# Test cases för Multiverse demo
checker = VulnCheckerIAM()
test_policy = '''
{
    "Statement": [{
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject"
    }]
}
'''
vulns = checker.check_policy_vulns(test_policy)
print(f"🚨 IAM Policy Analysis: {vulns}")
print(f"Severity: {checker.severity_score(vulns)}/10")
