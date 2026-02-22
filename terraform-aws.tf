provider "aws" {
  region = "eu-north-1"
}

# S3 Security Scanner Lambda
resource "aws_lambda_function" "s3_scanner" {
  filename      = "s3_scanner.zip"
  function_name = "csio-s3-guardduty"
  role          = aws_iam_role.lambda_role.arn
  handler       = "s3_scanner.lambda_handler"
  runtime       = "python3.11"
}

# OSCP Toolkit ECS Cluster
resource "aws_ecs_cluster" "oscp_cluster" {
  name = "csio-oscp-cluster"
}
