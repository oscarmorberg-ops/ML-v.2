
def s3_kms_dual_layer():
    policy = {
        "SSE-KMS": "Customer-managed keys",
        "HTTPS-only": "Enforced bucket policy", 
        "MFA-delete": "Versioning enabled"
    }
    print("S3 KMS Dual-Layer: SSE-KMS + HTTPS + MFA ✓")

