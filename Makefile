.PHONY: install test run lint clean

install:
	pip install -r requirements.txt

test:
	pytest tests/

run:
	streamlit run main.py

lint:
	flake8 .
	black --check .

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
