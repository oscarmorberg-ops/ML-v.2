cat > Dockerfile << 'EOF'
FROM python:3.11-slim

# Installera Lambda Runtime Interface Emulator
RUN pip install awslambdaric

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY
