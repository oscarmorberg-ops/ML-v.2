import streamlit as st
import random
from datetime import datetime

st.title("🛡️ CSIO Security Hub + GuardDuty SIMULATOR")
st.markdown("**LIVE Metrics | OSCP + Multiverse CSO Portfolio**")

# Simulerade GuardDuty detectors
detectors = random.randint(1, 3)
st.success(f"✅ GuardDuty ACTIVE: {detectors} detectors (eu-north-1)")
st.info("🛡️ Malware Protection: S3 + EC2 scanning")

# Simulerade Security Hub findings
high_findings = random.randint(2, 8)
medium_findings = random.randint(10, 25)
total_findings = high_findings + medium_findings

col1, col2, col3 = st.columns(3)
col1.metric("🔴 HIGH Severity", high_findings, f"+{random.randint(0,2)}")
col2.metric("🟡 MEDIUM Severity", medium_findings, f"-{random.randint(0,3)}")
col3.metric("📊 TOTAL Findings", total_findings)

st.subheader("🚀 Recent Alerts (LIVE)")
alerts = [
    f"S3 Malware Scan: bucket123 (HIGH) - {datetime.now().strftime('%H:%M')}",
    "EC2 Crypto Mining: i-123456789 (HIGH)",
    "Unusual IAM: root user login (MEDIUM)"
]
for alert in alerts:
    st.error(alert)

st.markdown("---")
st.success("🎉 **CSIO Beast Mode: 502 commits | Multiverse CSO READY!**")
