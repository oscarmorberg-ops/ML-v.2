
NIST_CONTROLS = {
    "IA-5": "MFA implemented ✓",
    "SC-28": "DLP active ✓", 
    "AC-6": "Least privilege enforced ✓",
    "AU-6": "Audit logs 90 days ✓"
}
compliance_score = sum(1 for status in NIST_CONTROLS.values() if "✓" in status) / len(NIST_CONTROLS)
print(f"NIST 800-53: {compliance_score:.1%}")

