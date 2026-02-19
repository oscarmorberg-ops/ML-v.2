scan:
	@echo "🔥 S3CyberScanner v4.3 - $(COMPANY)"
	@python3 s3_scanner.py $(COMPANY)

all: scan
