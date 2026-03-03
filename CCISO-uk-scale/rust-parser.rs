use std::collections::HashMap;
fn main() {
    let mut risks = HashMap::new();
    risks.insert("S3", 7.6);
    risks.insert("IAM", 6.8);
    println!("🇬🇧 CCISO Rust: S3={:.1}", risks["S3"]);
}
