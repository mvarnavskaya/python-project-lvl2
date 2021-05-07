install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 gendiff

pytest:
	poetry run pytest gendiff tests
	
test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml tests
	
run_test:
	poetry run pytest --cov=gendiff tests/ --cov-report xml
