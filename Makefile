.PHONY: help install test lint fmt type check build rubric clean

help:  ## Show this help
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
		awk 'BEGIN{FS=":.*?## "}{printf "  \033[36m%-10s\033[0m %s\n", $$1, $$2}'

install:  ## Install package + dev deps
	pip install -e ".[dev]"

test:  ## Run the test suite with coverage
	pytest --cov=clarion --cov-report=term-missing

lint:  ## Lint with ruff
	ruff check src tests

fmt:  ## Auto-format with ruff
	ruff format src tests
	ruff check --fix src tests

type:  ## Type-check with mypy
	mypy

check: lint type test  ## Run everything CI runs

build:  ## Compile the full system prompt to system.txt
	python -m clarion.cli build --profile full -o system.txt

rubric:  ## Regenerate the YAML mirror of the rubric
	python -m clarion.cli rubric --export yaml > clarion/rubric.yaml

clean:  ## Remove caches and build artifacts
	rm -rf build dist .pytest_cache .mypy_cache .ruff_cache .coverage htmlcov *.egg-info
