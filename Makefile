pip:
	pip-compile && pip-sync

pre-commit:
	pre-commit run --all-files

start:
	uvicorn ch01.main:app --reload
