
def threat_scoring_engine(alerts):
    scores = {"critical": 0, "high": 3, "medium": 12, "low": 5}
    total_risk = sum(count * severity for severity, count in scores.items())
    return f"Risk Score: {total_risk}/100 - High: {scores[\"high"]} alerts"

print(threat_scoring_engine({}))

