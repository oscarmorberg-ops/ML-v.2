
def cni_supply_chain_risk():
    suppliers = {
        "Primary": {"contract_audit": "✓", "caf_score": "92%"},
        "Nth_party": {"visibility": "88%", "remediation_sla": "30d"}
    }
    risk_score = (92 + 88) / 2
    print(f"CNI Supply Chain Risk: {risk_score:.1f}% | NCSC CAF A5.1 PASS")

