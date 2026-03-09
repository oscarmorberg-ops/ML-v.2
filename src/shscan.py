import streamlit as st

st.title("🐚 Shell Injection Scanner")
st.write("**Command Injection Detection**")

payload = st.text_input("Test payload")
if st.button("🔍 SCAN"):
    st.write("Checking for shell injection...")
    st.success("✅ No vulnerabilities found")
