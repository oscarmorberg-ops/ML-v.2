# NIST CSF 2.0 → AWS S3 Pipeline Mapping

## GOVERN
- IAM policy scanning (boto3)
- Least privilege violations  

## IDENTIFY (47 assets)
- S3 buckets: `list_buckets()`
- IAM users/roles
- EC2 instances + SQS

## PROTECT  
- S3 encryption: `get_bucket_encryption()`
- Public ACL hardening

## DETECT
- CloudWatch permission drift
- New public buckets

## RESPOND
- Lambda auto-private()

## RECOVER
- CloudTrail audit logs
