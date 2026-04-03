# Install all dependencies
install:
    uv sync --all-groups

# Run end-to-end tests
# Keep parity with the previous CI behavior.
test:
    uv run --group test pytest tests -m end_to_end --cov=./ --cov-report=xml -n auto

# Run type checking
typing:
    uv run --group typing --group test --isolated ty check

# Run linting and formatting
lint:
    uvx prek run -a

# Build docs
docs:
    uv run --group docs sphinx-build -n -T -b html -d docs/build/doctrees docs/source docs/build/html

# Run all checks
check: lint typing test
