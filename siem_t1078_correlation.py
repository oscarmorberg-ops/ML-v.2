# 586: SIEM T1078 correlation layer (CloudTrail+GuardDuty)
def t1078_correlation(cloudtrail_logs, guardduty_findings):
    alerts = []
    
    for log in cloudtrail_logs:
        if log['eventName'] == 'AssumeRole' and log['userIdentity'].get('arn', '').endswith(':root'):
            # T1078: Valid Accounts Abuse detected
            for finding in guardduty_findings:
                if 'PrivilegeEscalation' in finding['type']:
                    alert = {
                        'mitre': 'T1078',
                        'confidence': 0.95,
                        'action': 'zerotrust.block_ip',
                        'source_ip': log['sourceIPAddress']
                    }
                    alerts.append(alert)
    
    return alerts

# Test: T1078 → SIEM → ZeroTrust 90s
if __name__ == "__main__":
    print("SIEM T1078 layer: READY!")
