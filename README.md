# Building Python Microservices with FastAPI
***
Based on **Building Python Microserices with FastAPI - Sherwin John C. Tragura** [packt]

[Link to the book](https://www.packtpub.com/product/building-python-microservices-with-fastapi/9781803245966)

***
## Initial setup
- PyCharm Professional 2022.3
- Python 3.10
- setuptools 65.6.3
- wheels 0.38.4
- pre-commit 2.21.0
- flake8 6.0.0
- isort 5.11.4
- pip-tools 6.12.1

1. Install pip-compile
```shell
$ pip install pip-tools==6.12.1
$ make pip
```
2. Install pre-commit
```shell
$ pip install pre-commit==2.21.0
$ pre-commit install
$ make pre-commit
```
***
## Usefull commands:
Run application locally
```shell
$ cd ch01/
$ uvicorn main:app --reload

INFO:     Will watch for changes in these directories: ['~/fastapi-learning/ch01']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [123669] using WatchFiles
INFO:     Started server process [123671]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```
***

## Chapter 1
- Technical requirements
- Setting up the development environment
- Initializing and configuring FastAPI
