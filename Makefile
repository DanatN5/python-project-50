install:
	uv sync

build:
	uv build

run:
	uv run gendiff

package-install:
	uv tool install dist/*.whl

reinstall:
	uv tool install --force dist/*.whl

test:
	uv run pytest

test-coverage:
	uv run pytest --cov=gendiff --cov-report=xml:coverage.xml

lint:
	uv run ruff check

check: test lint

.PHONY: install test lint selfcheck check build
