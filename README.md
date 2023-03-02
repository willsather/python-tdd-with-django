# Python TDD with Django REST Framework

### Python REST DRF Learning Path

## Section 0: Introduction

This repository is in the works to create a series of Python / Django REST Framework / data science.

[`/docs`](./docs) contains the 7 different Markdown documents that respectively align with the 7 different directories
in the repository. Each directory contains an individual virtual environment and _should_ be able to be opened in any
editor to easily run the tests and server.

The hope of this repository and maybe future work is to create as close to a _real-world_ example to a data science
project as possible. The hope is to have this setup in a way that is easy to follow the path (or story) I took to
achieve this and well document it.

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

* Uses default values for database rows that don't have those columns (FEATURES!!)

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
- K8S configuration
- Simplify YAML using Tanzu Applications

