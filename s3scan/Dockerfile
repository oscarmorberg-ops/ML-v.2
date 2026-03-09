FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install streamlit==1.38.0 pandas numpy boto3 requests python-dotenv
EXPOSE 8501
CMD ["streamlit", "run", "src/s3scan.py", "--server.port=8501", "--server.address=0.0.0.0"]
