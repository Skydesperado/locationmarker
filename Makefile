.PHONY: check
check:
	cd backend && python manage.py check

.PHONY: runserver
runserver:
	cd backend && python manage.py runserver

.PHONY: migrations
migrations:
	cd backend && python manage.py makemigrations

.PHONY: migrate
migrate:
	cd backend && python manage.py migrate

.PHONY: superuser
superuser:
	cd backend && python manage.py createsuperuser

.PHONY: test
test:
	cd backend && python manage.py test
