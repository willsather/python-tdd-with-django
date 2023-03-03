# Python TDD with Django REST Framework

### Python REST DRF Learning Path

The goal of this repository is to create a series of content about building Python application using Django REST
Framework.

Also, the intent was to use this DRF application to service a data science / machine learning model, and create the
whole thing by TDDing in Python. The hope was to not only build out various stages of an application, but also
demonstrate _one_ strategy for writing tests for machine learning. In doing so, I goaled for creating as close to a _
real-world_ example to a data science project as possible, while documenting all the work I did building it. 

[`/docs`](./docs) contains the 7 different Markdown documents that respectively align with the 7 different directories
in the repository. Each directory contains an individual virtual environment and _should_ be able to be opened in any
editor to easily run the tests and server.

## Section 0: Introduction

- Why Python is important
- Primary Goals / Objectives
  - Maybe list out
- Overview on what is being built
- What is the endpoint about (`Penguins`)
- List of each section / respective topics

## Section 1: Setup Environment

- Create directories / git repo
- Install `Python` using Homebrew
- Create virtual environment with `venv`
- Install dependencies REST dependencies `Django` and `rest_framework`
- Install `pytest-django`

## Section 2: Setup Django

- Differences in Python web frameworks
- Database Discussion
- Structure of a Django application
- Creating project / app
- What is `manage.py`
- What is `urls.py` and `views.py` (Class Based Views)

## Section 3: TDD for Django Rest Framework GET Endpoint

- TDD
    - Write `GET` test with the `GET` endpoint (hardcoded value)
    - Create model and serializer
    - Database migration
        - `python manage.py makemigrations`
        - `python manage.py migrate`
    - Update `GET` test with the `GET` endpoint to get all penguins

## Section 4: TDD for Django Rest Framework CRUD Application

- Write `POST` test with the `POST` endpoint
- Add `PenguinDetailsController` using Generic
- Differences with `GenericAPIView` and `ListCreateAPIView`
    - Tests pass with either implementation (useful for refactoring)
- Ends with basic CRUD application that can `GET`,`POST`,`PUT`,`DELETE`

## Section 5: Machine Learning / Decision Trees

- Introduction to machine learning
    - Important terms and definitions
    - Common steps to create a model
- Create model using SciKit learn

## Section 6: TDD DRF Predict (using Decision Tree)

* Skips forward and adds 5 more properties to a penguin *

Note: Previously the `Penguin` object had only two properties, now there exists 5 more properties. To add properties,
you must do a db migration.

- TDD
    - Write `POST /predict` test with the `POST /predict` endpoint
        - Basic POST and returns a static value
    - Plop in exported model into code and use sci-kit learn `sk.predict` method
    - Write unit test for different cases of our custom business logic
        - Write test in `test_service.py` using `@pytest.mark.unit`
    - Write business logic in `service.py` that takes in input, and returns value using `sk.predict`
    - Update `test_views.py` to have test for `/predict` for a given penguin, returns type of penguin

## Section 7: Deploy Python Application using Docker and Kubernetes

- Python Application Containerization using Docker
  - Maybe using Cloud Native build packs?
- K8S configuration
- Simplify YAML using Tanzu Applications

