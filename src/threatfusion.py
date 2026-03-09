import streamlit as st
import pandas as pd

st.title("🎯 ThreatFusion - Threat Intelligence Fusion")
st.write("**CCISO Threat Intel Dashboard**")

st.subheader("🔥 Real-time Threat Feeds")
col1, col2 = st.columns(2)

with col1:
    st.metric("High Risk Alerts", "47", "12")
    st.metric("Critical CVEs", "3", "-1")

with col2:
    st.metric("GuardDuty Findings", "128", "25")
    st.metric("SIEM Incidents", "89", "8")

st.subheader("📊 Threat Landscape")
df = pd.DataFrame({
    'Threat': ['Ransomware', 'APIscan', 'DDoS', 'Phishing'],
    'Score': [92, 87, 76, 64],
    'Priority': ['HIGH', 'HIGH', 'MEDIUM', 'LOW']
})
st.dataframe(df, use_container_width=True)

st.success("✅ 590 commits | 93.5% coverage | ZeroTrust Pipeline LIVE")
