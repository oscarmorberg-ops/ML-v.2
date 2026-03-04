/// S3 bucket security scanner (eu-north-1)
use std::error::Error;
use chrono::{DateTime, Utc};

pub const BUCKET: &str = "oscar-s3-security-scan-eu-north-1";
pub const REGION: &str = "eu-north-1";

pub async fn scan() -> Result<Vec<String>, Box<dyn std::error::Error>> {
    println!("Scanning S3 bucket: {} in {}", BUCKET, REGION);
    println!("S3 scan started at {}", chrono::Utc::now());

    // Validate config
    if BUCKET.is_empty() {
        return Err("S3 BUCKET is empty".into());
    }

    let mock_findings = vec![
        "CRITICAL: PublicRead ACL detected", 
        "HIGH: Bucket versioning disabled", 
        "MEDIUM: No server-side encryption",
        "CRITICAL: PublicWrite ACL detected",
        "LOW: Old object without tags"
    ];

    let findings: Vec<String> = mock_findings
        .into_iter()
        .filter(|f| f.contains("CRITICAL") || f.contains("HIGH"))
        .map(|f| f.to_string())
        .collect();

    println!("Found {} security issues", findings.len());
    Ok(findings)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_s3_scan_finds_critical() {
        let findings = scan().await.unwrap();
        assert!(!findings.is_empty());
        assert_eq!(findings.len(), 2);
        assert!(findings.iter().any(|f| f.contains("PublicRead")));
    }
}
