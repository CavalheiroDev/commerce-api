PROJECT_NAME := commerce_api
PYTHON_VERSION := 3.9.12
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres

.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools
	pip install -r requirements-dev.txt

.create-venv:
	pyenv install -s $(PYTHON_VERSION)
	pyenv uninstall -f $(VENV_NAME)
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pyenv local $(VENV_NAME)

create-venv: .create-venv setup-dev

.clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +
	find . -name '*cache' -exec rm -rf {} +

.clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr reports/
	rm -fr .pytest_cache/
	rm -f coverage.xml

clean: .clean-build .clean-pyc .clean-test ## remove all build, test, coverage and Python artifacts

alembic-revision:
	alembic revision --autogenerate -m "auto"

alembic-upgrade-head:
	alembic upgrade head

alembic-upgrade-one:
	alembic upgrade +1

alembic-downgrade-one:
	alembic downgrade -1

alembic-downgrade-base:
	alembic downgrade base

alembic-history:
	alembic history -i


run-postgres:
	docker start commerce_api 2>/dev/null || docker run --name commerce_api -p "5432:5432" -e "POSTGRES_PASSWORD=commerce_api" -e "POSTGRES_USER=commerce_api" -e "POSTGRES_DB=commerce_api" -d postgres:13.6-bullseye

run-rabbit:
	docker start commerce_api_rabbit 2>/dev/null || docker run -d --name commerce_api_rabbit -e RABBITMQ_DEFAULT_VHOST=commerce_api -p 5672:5672 -p 15672:15672 rabbitmq:3.10-management
