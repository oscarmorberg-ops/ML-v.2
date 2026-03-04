use aws_sdk_s3::Client;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let config = aws_config::from_env()
        .region("eu-north-1")
        .load()
        .await;
    let client = Client::new(&config);
    let bucket = "min-cybersec-pipeline-2026";

    match client.list_objects_v2().bucket(bucket).send().await {
        Ok(resp) => {
            let objects = resp.contents();
            println!("✅ {}: {} objects", bucket, objects.len());
            for obj in objects {
                if let Some(key) = obj.key() {
                    println!("  📄 {}", key);
                }
            }
        }
        Err(e) => println!("❌ Error: {:?}", e),
    }
    Ok(())
}

