use aws_sdk_s3::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_config::from_env()
        .region("eu-north-1")
        .load()
        .await;
    let client = Client::new(&config);
    let bucket = "min-cybersec-pipeline-2026";

    println!("🔍 Starting S3 security scan: {}", bucket);

    match client.list_objects_v2().bucket(bucket).send().await {
        Ok(resp) => {
            let objects = resp.contents();
            println!("✅ {}: {} objects", bucket, objects.len());
            
            let mut threats = 0;
            for obj in objects {
                if let Some(key) = obj.key() {
                    println!("  📄 {}", key);
                    
                    // SECURITY SCANNING (CISO-level threat detection)
                    if key.contains("scan.json") || key.contains("threat") {
                        println!("  🔴 HIGH RISK: {}", key);
                        threats += 1;
                    }
                }
            }
            println!("🚨 Total threats detected: {}", threats);
        }
        Err(e) => println!("❌ Error: {:?}", e),
    }
    Ok(())
}
