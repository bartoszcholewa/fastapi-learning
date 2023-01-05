pip:
	pip-compile && pip-sync

pre-commit:
	pre-commit run --all-files

start1:
	uvicorn ch01.main:app --reload

start2:
	uvicorn ch02.main:app --workers 5 --reload

start3:
	cd ch03 && uvicorn main:app --reload

start4:
	cd ch04 && uvicorn main:app --reload

start5a:
	cd ch05a && uvicorn main:app --reload

start5b:
	cd ch05b && uvicorn main:app --reload

start6:
	cd ch06 && uvicorn main:app --reload

start7a:
	cd ch07 && uvicorn main_a:app --reload

start7b:
	cd ch07 && uvicorn main_b:app --reload

start7c:
	cd ch07 && uvicorn main_c:app --reload

start7d:
	cd ch07 && uvicorn main_d:app --reload
