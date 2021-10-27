.PHONY:	help	lint-python	format-python	type-python

help:
	@echo "lint-python       -    Python Lint by Flake8."
	@echo "format-python     -    Python code format by Black."
	@echo "type-python     -    Python type check by mypy."

lint-python:
	flake8 .

format-python:
	black .

type-python:
	mypy .
