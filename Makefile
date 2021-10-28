.PHONY:	help	lint-python	format-python	type-python	format-js

help:
	@echo "lint-python       -    Python Lint by Flake8."
	@echo "format-python     -    Python code format by Black."
	@echo "type-python       -    Python type check by mypy."
	@echo "format-js         -    JS code format by Black."

lint-python:
	flake8 .

format-python:
	black .

format-js:
	./node_modules/prettier/bin-prettier.js --write ./seism-jp/static/js/*.js

type-python:
	mypy .
