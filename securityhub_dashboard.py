import streamlit as st
import boto3
hub = boto3.client('securityhub', region_name='eu-north-1')
detectors = boto3.client('guardduty', region_name='eu-north-1')

st.title("🛡️ CSIO Security Hub + GuardDuty")
findings = hub.get_findings(FilterConfig={})
st.metric("High Severity Findings", len([f for f in findings['Findings'] if f['Severity']['Label']=='HIGH']))
st.write("GuardDuty LIVE!")
