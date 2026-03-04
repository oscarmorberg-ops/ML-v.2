pub const BUCKET: &str = "oscar-guardduty-findings-eu-north-1";

pub async fn scan() -> Result<Vec<String>, Box<dyn std::error::Error>> {
    println!("Scanning GuardDuty: {}", BUCKET);
    Ok(vec!["CRITICAL: Backdoor".to_string()])
}
