import streamlit as st
import boto3
import os
from time import time
import psutil

st.title("🚀 CSIO S3 ML Auto-Scanner v2")
st.markdown("**LIVE ML Security Scanner** - Oscar Morberg | 502 commits UK TOP 7%")

# VERSION INFO (CSIO production standard)
VERSION = "v2.3.0"
BUILD_SHA = "5b7ab27"
COMMIT_COUNT = "502"

# AWS credentials
if "aws_configured" not in st.session_state:
    st.session_state.aws_configured = False

# METRICS FUNCTION
def get_metrics():
    start = time()
    return {
        'cpu_percent': psutil.cpu_percent(interval=0.1),
        'memory_percent': psutil.virtual_memory().percent,
        'response_time_ms': round((time() - start) * 1000, 2),
        's3_buckets_scanned': st.session_state.get('buckets_count', 0),
        'scanner_uptime': time()
    }

# LIVE METRICS + VERSION DASHBOARD
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("CPU", f"{psutil.cpu_percent():.1f}%")
with col2:
    st.metric("RAM", f"{psutil.virtual_memory().percent:.1f}%")
with col3:
    st.metric("Response Time", f"{get_metrics()['response_time_ms']:.1f}ms")

col4, col5, col6 = st.columns(3)
with col4:
    st.metric("Version", VERSION)
with col5:
    st.metric("Commit", BUILD_SHA[:7])
with col6:
    st.metric("Commits", COMMIT_COUNT)

if st.button("🔑 Konfigurera AWS (privata keys)"):
    st.session_state.AWS_ACCESS_KEY_ID = st.text_input("Access Key ID", type="password")
    st.session_state.AWS_SECRET_ACCESS_KEY = st.text_input("Secret Key", type="password")
    st.session_state.aws_configured = True

if st.session_state.aws_configured:
    region = st.selectbox("AWS Region", ['eu-north-1', 'us-east-1', 'eu-west-1'])
    
    if st.button("🔍 **SCAN S3 BUCKETS LIVE** 🚀", type="primary"):
        try:
            os.environ['AWS_ACCESS_KEY_ID'] = st.session_state.AWS_ACCESS_KEY_ID
            os.environ['AWS_SECRET_ACCESS_KEY'] = st.session_state.AWS_SECRET_ACCESS_KEY
            os.environ['AWS_DEFAULT_REGION'] = region

            with st.spinner("Scanning LIVE S3 buckets..."):
                s3 = boto3.client('s3')
                buckets = s3.list_buckets()
                
                st.session_state.buckets_count = len(buckets['Buckets'])
                st.success(f"✅ **Found {st.session_state.buckets_count} LIVE S3 buckets!**")
                st.balloons()

                for bucket in buckets['Buckets']:
                    st.code(f"📦 {bucket['Name']}")

        except Exception as e:
            st.error(f"❌ AWS Error: {str(e)}")

st.info("👈 AWS keys → Region → SCAN → LIVE metrics + S3 resultat!")
