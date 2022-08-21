PROJECT_NAME := commerce_api
PYTHON_VERSION := 3.9.12
VENV_NAME := $(PROJECT_NAME)-$(PYTHON_VERSION)
DATABASE_PASS := postgres

.pip:
	pip install pip --upgrade

setup-dev: .pip
	pip uninstall -y typing
	pip install -U setuptools
	-apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
	-sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
	pip install -r requirements-dev.txt

setup: .pip
	pip uninstall -y typing
	pip install -U setuptools
	-apk --update --upgrade add gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev
	-sudo apt-get install build-essential python3-dev python3-pip python3-setuptools python3-wheel python3-cffi libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info
	pip install -r requirements.txt

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

black:
	echo "Running black"
	black --check .

flake8:
	echo "Running flake8"
	flake8

mypy:
	echo "Running mypy"
	mypy .

code-convention: black flake8 mypy

test:
	# "Running unit tests"
	 pytest -v --cov-report=term-missing --cov-report=html --cov-report=xml --cov=nix_proxy --cov-fail-under=80
