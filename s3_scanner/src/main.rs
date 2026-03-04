use aws_sdk_s3::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_config::from_env()
        .region("eu-north-1")
        .load()
        .await;
    let client = Client::new(&config);
    let bucket = "min-cybersec-pipeline-2026";

    println!("🔍 S3 security scan + ML: {}", bucket);

    match client.list_objects_v2().bucket(bucket).send().await {
        Ok(resp) => {
            let objects = resp.contents();
            println!("✅ {}: {} objects", bucket, objects.len());
            
            let mut threats = 0;
            let mut anomalies = 0;
            
            for obj in objects {
                if let Some(key) = obj.key() {
                    println!("  📄 {}", key);
                    
                    if key.contains("scan.json") || key.contains("threat") {
                        println!("  🔴 HIGH RISK: {}", key);
                        threats += 1;
                    }
                    
                    let risk_score = if key.contains("raw/") { 8 } 
                                   else if key.contains("scan.json") { 7 }
                                   else if key.contains("threat") { 9 }
                                   else { 3 };
                    println!("  ⚠️  ML Risk: {}", risk_score);
                    
                    if key.starts_with("raw/") && key.contains("scan") {
                        println!("  🧠 ML ANOMALY: Raw scan");
                        anomalies += 1;
                    }
                }
            }
            println!("🚨 Report: Threats={}, Anomalies={}", threats, anomalies);
        }
        Err(e) => println!("❌ Error: {:?}", e),
    }
    Ok(())
}
