run:
	python manage.py runserver

migration:
	python manage.py makemigrations
	python manage.py sqlmigrate razTravel 0002
	python manage.py migrate
	

