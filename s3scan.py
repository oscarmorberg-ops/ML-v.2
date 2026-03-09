#!/usr/bin/env python3
import os
os.system("streamlit run src/s3scan.py --server.port=8501 --server.address=0.0.0.0 &")
print("🌐 S3 Scanner LIVE → http://localhost:8501")
