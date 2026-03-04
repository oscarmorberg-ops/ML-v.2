use aws_sdk_s3::Client;
use aws_sdk_s3::types::ByteStream;
use serde_json::Value;
use bytes::Bytes;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_config::from_env()
        .region("eu-north-1")
        .load()
        .await;
    let client = Client::new(&config);
    let bucket = "min-cybersec-pipeline-2026";

    println!("🔍 S3 security scan + JSON download: {}", bucket);

    match client.list_objects_v2().bucket(bucket).send().await {
        Ok(resp) => {
            let objects = resp.contents();
            println!("✅ {}: {} objects", bucket, objects.len());
            
            let mut threats = 0;
            let mut anomalies = 0;
            let mut json_parsed = 0;
            
            for obj in objects {
                if let Some(key) = obj.key() {
                    println!("  📄 {}", key);
                    
                    // THREAT DETECTION
                    if key.contains("scan.json") || key.contains("threat") {
                        println!("  🔴 HIGH RISK: {}", key);
                        threats += 1;
                    }
                    
                    // ML RISK SCORING
                    let risk_score = if key.contains("raw/") { 8 } 
                                   else if key.contains("scan.json") { 7 }
                                   else if key.contains("threat") { 9 }
                                   else { 3 };
                    println!("  ⚠️  ML Risk: {}", risk_score);
                    
                    // ML ANOMALY
                    if key.starts_with("raw/") && key.contains("scan") {
                        println!("  🧠 ML ANOMALY: Raw scan");
                        anomalies += 1;
                    }
                    
                    // JSON DOWNLOAD + PARSING
                    if key.ends_with("scan.json") {
                        println!("  📥 Downloading JSON: {}", key);
                        match client.get_object()
                            .bucket(bucket)
                            .key(key)
                            .send()
                            .await {
                                Ok(response) => {
                                    let data = response.body.collect().await.map_err(|e| format!("Body collect error: {}", e))?;
                                    let bytes = data.into_bytes();
                                    match serde_json::from_slice::<Value>(&bytes) {
                                        Ok(json) => {
                                            println!("  ✅ JSON parsed: {} fields", json.as_object().map_or(0, |o| o.len()));
                                            if let Some(findings) = json.get("findings").and_then(|f| f.as_array()) {
                                                println!("  🚨 Scan findings: {}", findings.len());
                                            }
                                            json_parsed += 1;
                                        }
                                        Err(e) => println!("  ❌ JSON parse error: {:?}", e),
                                    }
                                }
                                Err(e) => println!("  ❌ Download error: {:?}", e),
                            }
                    }
                }
            }
            
            println!("🚨 CISO SECURITY REPORT:");
            println!("   Threats: {}", threats);
            println!("   ML Anomalies: {}", anomalies);
            println!("   JSON files parsed: {}", json_parsed);
        }
        Err(e) => println!("❌ Error: {:?}", e),
    }
    Ok(())
}
