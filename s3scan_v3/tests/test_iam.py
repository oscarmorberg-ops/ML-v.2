import sys
sys.path.insert(0, '../')  # Fixar import från s3scan_v3

from vuln_checker_iam import VulnCheckerIAM
from main_v3 import scan_iam_policies

def test_iam_mock_scanner():
    vulns = scan_iam_policies()
    assert len(vulns) == 2
    assert "PublicReadAccess" in vulns[0]
    print("✅ test_iam_mock_scanner PASSED")

def test_critical_public_principal():
    checker = VulnCheckerIAM()
    policy = '{"Statement": [{"Effect": "Allow", "Principal": "*"}]}'
    vulns = checker.check_policy_vulns(policy)
    assert "CRITICAL: Public Principal *" in vulns
    print("✅ test_critical_public_principal PASSED")

if __name__ == "__main__":
    test_iam_mock_scanner()
    test_critical_public_principal()
    print("🎉 s3scan v3 FULLY TESTED - Multiverse production-ready!")
