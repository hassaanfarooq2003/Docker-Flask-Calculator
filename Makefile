pylint:
	pylint app.py --disable c,r

install:
	pip install -r requirements.txt

run:
	python app.py

test:
	python test.py	