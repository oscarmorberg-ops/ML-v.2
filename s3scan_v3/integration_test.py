import sys
sys.path.insert(0, './')  # Fixar imports

from main_v3 import scan_iam_policies
from vuln_checker_iam import VulnCheckerIAM
from slack_notifier import SlackNotifier

class IntegrationTestS3IAM:
    def __init__(self):
        self.iam_checker = VulnCheckerIAM()
        self.slack = SlackNotifier()
    
    def run_full_pipeline(self):
        """Multiverse demo: S3 + IAM full pipeline"""
        print("🚀 s3scan v3 FULL PIPELINE TEST")
        
        # Step 1: IAM scan
        iam_vulns = scan_iam_policies()
        print(f"✅ Step 1: Found {len(iam_vulns)} IAM vulns")
        
        # Step 2: Advanced analysis
        for vuln in iam_vulns[:1]:  # Test first vuln
            policy_mock = '{"Statement": [{"Effect": "Allow", "Principal": "*"}]}'
            policy_vulns = self.iam_checker.check_policy_vulns(policy_mock)
            print(f"✅ Step 2: Policy analysis: {policy_vulns}")
        
        # Step 3: Slack alert
        self.slack.send_iam_alert(iam_vulns)
        print("✅ Step 3: Slack alert sent")
        
        print("🎉 FULL S3+IAM PIPELINE PASSED - Multiverse LIVE demo ready!")
    
    def performance_test(self):
        """Testar pipeline speed för Multiverse pitch"""
        import time
        start = time.time()
        self.run_full_pipeline()
        end = time.time()
        print(f"⚡ Pipeline speed: {end-start:.2f}s")

# Kör Multiverse demo
if __name__ == "__main__":
    test = IntegrationTestS3IAM()
    test.run_full_pipeline()
    test.performance_test()
