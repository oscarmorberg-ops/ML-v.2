#!/bin/bash
echo "📁 Dir: ~/cybersec-s3-pipeline"
echo "💾 Git status: "
git status
echo "☁️  AWS ready: aws --version"
read -p "Commit message: " msg
git add . && git commit -m "$msg" && git push
echo "✅ PUSHAD till oscarmorberg-ops/cybersec-s3-pipeline!"
