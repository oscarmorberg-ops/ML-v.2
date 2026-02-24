import streamlit as st
import boto3
import os

st.title("🚀 CSIO S3 ML Auto-Scanner v2")
st.markdown("**LIVE ML Security Scanner** - Oscar Morberg")

# AWS credentials
if "aws_configured" not in st.session_state:
    st.session_state.aws_configured = False

if st.button("🔑 Konfigurera AWS (privata keys)"):
    st.session_state.AWS_ACCESS_KEY_ID = st.text_input("Access Key ID", type="password")
    st.session_state.AWS_SECRET_ACCESS_KEY = st.text_input("Secret Key", type="password")
    st.session_state.aws_configured = True

if st.session_state.aws_configured:
    if st.button("🔍 **SCAN S3 BUCKETS LIVE** 🚀", type="primary"):
        try:
            os.environ['AWS_ACCESS_KEY_ID'] = st.session_state.AWS_ACCESS_KEY_ID
            os.environ['AWS_SECRET_ACCESS_KEY'] = st.session_state.AWS_SECRET_ACCESS_KEY
            os.environ['AWS_DEFAULT_REGION'] = 'eu-north-1'

            s3 = boto3.client('s3')
            buckets = s3.list_buckets()

            st.success(f"✅ **Found {len(buckets['Buckets'])} LIVE S3 buckets!**")
            st.balloons()

            for bucket in buckets['Buckets']:
                st.code(f"📦 {bucket['Name']}")

        except Exception as e:
            st.error(f"❌ AWS Error: {str(e)}")

st.info("👈 Ange dina AWS keys → SCAN → LIVE resultat!")
