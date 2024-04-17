PHONY += up
up:
	python manage.py runserver 5000 

PHONY += fresh
fresh:
	pip install -r ./backend/requirements.txt 
	python manage.py runserver 5000 

PHONY += migrate
migrate:
	python manage.py makemigrations
	python manage.py migrate 
	
