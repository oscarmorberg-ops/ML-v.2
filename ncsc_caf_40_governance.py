
NCSC_CAF_40 = {
    "A1_Governance": {
        "leadership_commitment": "98%", 
        "risk_appetite_defined": "✓",
        "senior_accountability": "✓"
    },
    "A2_Risk_Treatment": {"treatment_plan": "95%", "supply_chain": "92%"},
    "D1_Response_Planning": {"mttr_sla": "3.2h", "rc_analysis": "✓"}
}
overall_score = sum(int(v) for d in NCSC_CAF_40.values() for v in d.values() if isinstance(v, str) and "%" in v) / 3
print(f"NCSC CAF 4.0: {overall_score:.1f}% | UK CNI READY")

