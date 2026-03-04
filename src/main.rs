use tokio;

mod s3;
mod guardduty;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    println!("🚀 CyberSec S3 Pipeline Starting...");
    println!("Scanning S3 buckets + GuardDuty findings...");
    
    // Kör båda scannrarna parallellt med tokio::join!
    let (s3_results, guardduty_results) = tokio::join!(
        s3::scan(),
        guardduty::scan()
    );

    let s3_findings = s3_results?;
    let guardduty_findings = guardduty_results?;

    println!("📊 SECURITY SCAN SUMMARY:");
    println!("═══════════════════════════════");
    println!("S3 Security Issues:   {}", s3_findings.len());
    println!("GuardDuty Findings:   {}", guardduty_findings.len());
    println!("TOTAL CRITICAL:       {}", s3_findings.len() + guardduty_findings.len());
    println!("═══════════════════════════════");

    // Lista alla findings
    if !s3_findings.is_empty() {
        println!("🔴 S3 ISSUES:");
        for issue in &s3_findings {
            println!("  - {}", issue);
        }
    }

    if !guardduty_findings.is_empty() {
        println!("🔴 GUARDDUTY FINDINGS:");
        for finding in &guardduty_findings {
            println!("  - {}", finding);
        }
    }

    println!("✅ Scan complete!");
    Ok(())
}
