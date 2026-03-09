#!/usr/bin/env python3
import os
os.system("streamlit run src/mlscan.py --server.port=8504 --server.address=0.0.0.0 &")
print("🤖 ML Scanner LIVE → http://localhost:8504")
