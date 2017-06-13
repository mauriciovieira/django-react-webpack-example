db:
		dropdb --if-exists app_local
		createdb app_local
		dropuser --if-exists app
		createuser -s app

makemigrations:
		DJANGO_SETTINGS_MODULE=config.settings.local python manage.py makemigrations

migrate:
		DJANGO_SETTINGS_MODULE=config.settings.local python manage.py migrate

start-django:
		DJANGO_SETTINGS_MODULE=config.settings.local python manage.py runserver 8001

compile-react:
		npm run build

watch-react:
		npm run watch