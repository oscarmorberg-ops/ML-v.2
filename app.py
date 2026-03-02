import streamlit as st
from risk_score import calculate_risk_score
from metrics.version import get_version_info
import random

# Streamlit config
st.set_page_config(page_title="S3 CSIO Risk Dashboard", page_icon="🛡️", layout="wide")

st.title("🛡️ S3 OWASP Top 10 Risk Dashboard")
st.markdown("**CSIO-nivå security scanning**")

# Version info
version = get_version_info()
col1, col2, col3 = st.columns(3)
with col1: st.metric("Commits", version['commit_count'])
with col2: st.metric("Version", version['commit_sha'][:7])
with col3: st.caption("UK TOP 6% Cybersecurity")

# Mock buckets för demo (inga AWS keys behövs)
demo_buckets = [
    "test-prod-data", "legacy-backup-2024", "public-downloads", 
    "dev-app-files", "staging-media", "secure-archive",
    "open-logs", "unencrypted-backup", "team-documents"
]

st.header("🚨 Risk Scoring (0-100)")
st.markdown("**Demo mode - production ready**")

# Risk Dashboard
for bucket_name in demo_buckets:
    with st.container():
        col1, col2, col3, col4 = st.columns([2, 1, 1, 4])
        
        with col1:
            st.subheader(bucket_name)
        
        with col2:
            risk = calculate_risk_score(bucket_name)
            st.metric("Risk", f"{risk['risk_score']}/100")
        
        with col3:
            st.markdown(f"**{risk['risk_level']}**")
            st.markdown(risk['color'])
        
        with col4:
            for finding in risk['findings']:
                st.caption(f"• {finding}")

# Executive Summary
st.header("📊 Executive Summary")
col1, col2, col3 = st.columns(3)
high_risk = sum(1 for b in demo_buckets if calculate_risk_score(b)['risk_score'] > 70)
med_risk = sum(1 for b in demo_buckets if 30 <= calculate_risk_score(b)['risk_score'] <= 70)
with col1: st.metric("HIGH Risk", high_risk)
with col2: st.metric("MEDIUM Risk", med_risk)
with col3: st.metric("Total Scanned", len(demo_buckets))

st.markdown("---")
st.caption("🚀 Oscar Morberg | Multiverse CSO Portfolio | Demo Mode")
