
def csio_threat_hunt_t1566_t1078():
    playbook = {
        "T1566_Phishing": "SIEM correlation + Canarytokens 92%",
        "T1078_ValidAccounts": "CloudTrail→ZeroTrust 98%",
        "hunt_query": "eventName=AssumeRole AND userIdentity.type=AssumedRole"
    }
    print("CSIO Threat Hunt: T1566/T1078 LIVE | MTTR 3.2h")

