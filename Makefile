all:

run:
	pipenv run python main.py

upload:
	python setup.py sdist upload

