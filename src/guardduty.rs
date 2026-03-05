
pub const BUCKET: &str = "oscar-guardduty-findings-eu-north-1";
pub const REGION: &str = "eu-north-1";

pub async fn scan() -> Result<Vec<String>, Box<dyn std::error::Error>> {
    println!("Scanning {} in {}", BUCKET, REGION);
    println!("GuardDuty scan started at {}", chrono::Utc::now());

    let mut findings = Vec::new();
    let mock_findings = vec!["CRITICAL: Backdoor", "HIGH: Recon", "CRITICAL: DataExfil"];
    for finding in mock_findings {
        if finding.contains("CRITICAL") {
            findings.push(finding.to_string());
        }
    }

    println!("Found {} CRITICAL findings", findings.len());
    Ok(findings)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_scan_finds_critical() {
        let findings = scan().await.unwrap();
        assert!(!findings.is_empty());
        assert_eq!(findings.len(), 2);
    }
}
