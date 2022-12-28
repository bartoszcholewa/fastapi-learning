pip:
	pip-compile && pip-sync

pre-commit:
	pre-commit run --all-files
