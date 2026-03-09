FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install streamlit==1.38.0 pandas numpy boto3 requests python-dotenv
EXPOSE 8504
CMD ["streamlit", "run", "src/mlscan.py", "--server.port=8504", "--server.address=0.0.0.0"]
