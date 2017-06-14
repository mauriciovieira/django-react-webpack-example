install-local:
	pip install -r requirements/local.txt

db:
	dropdb --if-exists app_local
	createdb app_local
	dropdb --if-exists app_testing
	createdb app_testing
	dropuser --if-exists app
	createuser -s app

makemigrations:
	DJANGO_SETTINGS_MODULE=config.settings.local python manage.py makemigrations

migrate:
	DJANGO_SETTINGS_MODULE=config.settings.local python manage.py migrate

seed:
	DJANGO_SETTINGS_MODULE=config.settings.local python manage.py seed api --number=15

show-urls:
	DJANGO_SETTINGS_MODULE=config.settings.local python manage.py show_urls

test-django:
	DJANGO_SETTINGS_MODULE=config.settings.testing python manage.py test

start-django:
	DJANGO_SETTINGS_MODULE=config.settings.local python manage.py runserver 8001

compile-react:
	npm run build

watch-react:
	npm run watch

test-react:
	npm t