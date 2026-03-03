// UK CCISO Rust Parser v2 - S3 metrics extraction
use std::collections::HashMap;

fn main() {
    let mut risks = HashMap::new();
    risks.insert("S3 Encryption", 7.6);
    risks.insert("IAM Limits", 6.8);
    
    println!("🇬🇧 CCISO Rust Metrics:");
    for (k, v) in risks {
        println!("  {}: {:.1}/10", k, v);
    }
}
