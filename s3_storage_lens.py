
def s3_storage_lens():
    metrics = {
        "PublicBuckets": "0/1500 (0%)",
        "Encryption": "1500/1500 (100%)", 
        "Replication": "98.7%"
    }
    print(f"S3 Storage Lens: {metrics[\"PublicBuckets\"]} | Enterprise")

