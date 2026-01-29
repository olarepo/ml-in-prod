.PHONY: setup test lint format run smoke

setup:
	python -m venv .venv
	. .venv/bin/activate && pip install --upgrade pip
	. .venv/bin/activate && pip install -e .[dev]

test:
	pytest

lint:
	ruff src tests

format:
	black src tests

run:
	uvicorn deployment.azure_functions.function_app:app --reload

smoke:
	python scripts/smoke_test.py
