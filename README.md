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

## Chapter 1 - Setting Up FastAPI for Starters

- Technical requirements
- Setting up the development environment
- Initializing and configuring FastAPI
- Designing and implementing REST APIs
- Managing user requests and server response
- Handling form parameters
- Managing cookies

## Chapter 2 - Exploring the Core Fatures

- Technical requirements
- Structuring and organizing huge projects
- Managing API-related exception
- Converting objects to JSON-compatible types
- Managing API responses
- Creating background processes
- Using asynchronous path operations
- Applying middleware to filter path operations

## Chapter 3 - Investigating Dependency Injection

- Applying IoC/DI
- Exploring ways of injecting dependencies
- Organizing a project based on dependencies
- Using third-party containers
- Scoping of dependable

## Chapter 4 - Building the Microservice Application

- Applying the decomposition pattern
- Mounting the submodules
- Creating a common gateway
- Implementing the main endpoint
- Evaluating the microservice ID
- Applying the exception handlers
- Centralizing te logging mechanism
- Building the logging middleware
- Using the httpx module
- Using the requests module
- Applying the domain modeling approach
- Creating the layers
- Identifying the domain models
- Building the repository and service layers
- Managing a microservice's configuration details

## Chapter 5 - Connecting to a Relational Database

- Preparing for database connectivity
- Creating CRUD transactions using SQLAlchemy
- Implementing async CRUD transactions using SQLAlchemy
- Using GINO for async transactions
- Using Pony ORM for the repository layer
- Building the repository using Peewee
- Applying the CQRS design pattern

# Chapter 6 - Using a Non-Relational Database

- Setting up the database environment
- Applying the PyMongo driver for synchronous connections
- Creating async CRUD transactions using Motor
- Implementing CRUD transactions using MongoEngine
