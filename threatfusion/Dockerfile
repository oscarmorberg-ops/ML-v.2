FROM python:3.12-slim
WORKDIR /app
COPY . .
RUN pip install streamlit==1.38.0 pandas numpy boto3 requests python-dotenv
EXPOSE 8508
CMD ["streamlit", "run", "src/threatfusion.py", "--server.port=8508", "--server.address=0.0.0.0"]
