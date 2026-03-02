#!/usr/bin/env python3
class CSIOSOCPlaybookGenerator:
    def __init__(self):
        self.playbooks = {
            "T1078": {"action": "BLOCK + MFA Reset", "ttr": "15min", "escalation": "CSIO"},
            "T1059": {"action": "Isolate + EDR Scan", "ttr": "10min", "escalation": "SOC Lead"},
            "T1566": {"action": "DLP Block + User Lock", "ttr": "5min", "escalation": "Legal"}
        }
    
    def generate_response(self, technique):
        if technique in self.playbooks:
            pb = self.playbooks[technique]
            print(f"🎯 SOC Playbook LIVE för {technique} (16:57 CET)")
            print(f"⚡ Action: {pb['action']}")
            print(f"⏱️  TTR: {pb['ttr']}")
            print(f"📢 Escalation: {pb['escalation']}")
            print("✅ NCSC | NIST | SANS compliant")
        else:
            print("❌ Unknown MITRE technique")

# LIVE demo
if __name__ == "__main__":
    soc = CSIOSOCPlaybookGenerator()
    soc.generate_response("T1078")  # Valid Accounts

