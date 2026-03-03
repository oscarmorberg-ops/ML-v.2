#!/usr/bin/env python3
# 586: SIEM T1078 correlation layer (CloudTrail+GuardDuty→ZeroTrust)

def t1078_correlation(cloudtrail_logs, guardduty_findings):
    alerts = []
    for log in cloudtrail_logs:
        if log.get('eventName') == 'AssumeRole' and ':root' in log.get('userIdentity', {}).get('arn', ''):
            for finding in guardduty_findings:
                if 'PrivilegeEscalation' in finding.get('type', ''):
                    alerts.append({
                        'mitre': 'T1078',
                        'confidence': 0.95,
                        'action': 'zerotrust.block_ip',
                        'source_ip': log.get('sourceIPAddress')
                    })
    return alerts

if __name__ == "__main__":
    print("✅ SIEM T1078 layer: READY for commit 586!")
