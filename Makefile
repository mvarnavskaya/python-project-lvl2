install:
	poetry install

build:
	@poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

selfcheck: ## Checks the validity of the pyproject.toml file
	poetry check

make lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest gendiff tests
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests/
	
test:
	poetry run coverage run --source=gendiff -m pytest tests
