pip:
	pip-compile && pip-sync

pre-commit:
	pre-commit run --all-files

start1:
	uvicorn ch01.main:app --reload

start2:
	uvicorn ch02.main:app --workers 5 --reload
