FROM python:3.11-slim
WORKDIR /oscp-toolkit
COPY . .
RUN pip install requests pwntools
RUN chmod +x *.py
CMD ["python3", "oscp_dashboard.py"]
