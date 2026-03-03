
import json
def cloudtrail_anomaly_detector(event):
    suspicious = event.get("eventName") in ["AssumeRole", "CreatePolicyVersion"]
    user_anomaly = event.get("userIdentity", {}).get("type") == "AssumedRole"
    return {"suspicious": suspicious or user_anomaly, "risk_score": 0.92}

# Exempel CloudTrail event
sample_event = {"eventName": "AssumeRole", "userIdentity": {"type": "AssumedRole"}}
print(cloudtrail_anomaly_detector(sample_event))

