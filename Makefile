.PHONY: dev test deploy lint

dev:
	poetry install
	poetry run python ml_app.py

test:
	poetry run pytest tests/

deploy:
	aws ec2 run-instances --image-id ami-0abcdef1234567890 --count 1 --instance-type t2.micro --key-name ML-v2-key --user-data file://deploy.sh

lint:
	poetry run black .
	poetry run flake8 .
