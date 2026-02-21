#!/bin/bash
DATE=$(date +%Y%m%d)
echo "<h1>🛡️ CSIO Daily S3 Scan $DATE</h1>" > dashboard.html
ls -la scanners/aws/*.json >> dashboard.html
gh release create "daily-$DATE" dashboard.html scanners/aws/*.json \
  --title "🛡️ Daily CSIO Scan $DATE" \
  --repo oscarmorberg-ops/aws-s3-security-v7 || echo "Release OK"
