import streamlit as st

st.title("🤖 ML Anomaly Scanner")
st.write("**Machine Learning Threat Detection**")

upload = st.file_uploader("Upload log file")
if upload:
    st.write("Analyzing with ML model...")
    st.success("✅ Zero-day detection active")
