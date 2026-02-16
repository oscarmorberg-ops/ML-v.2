def scan_guardduty_findings():
    gd = boto3.client('guardduty')
    detectors = gd.list_detectors()
    detector_id = detectors['DetectorIds']["7cce33799064eaa5d7bbbaecb6ddab3b"]  # cb6ddab3b...
    findings = gd.list_findings(DetectorId=detector_id)
    print(f"CSIO GuardDuty: {len(findings['FindingIds'])} findings")
    return findings

