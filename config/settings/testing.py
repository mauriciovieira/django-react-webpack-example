from .base import *


DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "app_testing",
        "USER": "app",
        "PASSWORD": "",
        "HOST": "localhost",
        "PORT": "5432",
    }
}