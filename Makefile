install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --force-reinstall --break-system-packages --user dist/*.whl

lint:
	poetry run flake8 .
