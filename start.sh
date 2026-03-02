#!/bin/bash
echo "🚀 CYBERSEC BEAST MODE - S3 Risk Dashboard"
echo "=============================================="

# Git status
echo "📁 Dir: $(pwd)"
echo "💾 Git status: "
git status --short

# AWS ready check
if command -v aws &> /dev/null; then
    echo "☁️  AWS ready: $(aws --version | cut -d' ' -f1)"
else
    echo "☁️  Installera: pip install awscli"
fi

echo ""
echo "🚀 Kör:"
echo "   s3scan           # Risk Dashboard (localhost:8501)"
echo "   source venv/bin/activate && python3 -m streamlit run app.py"
echo "   git add . && git commit -m '...' && git push"
echo ""
echo "====================== READY! 🚀 ======================"
