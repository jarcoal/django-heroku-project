import os

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = True
INTERNAL_IPS = ('127.0.0.1',)

STATIC_URL = '/static/'

#S3
AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'static/media/')
MEDIA_URL = '/static/media/'

DEBUG_TOOLBAR_CONFIG = { 'INTERCEPT_REDIRECTS': False, }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(PROJECT_PATH, '../../db.sqlite3'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

DOMAIN = 'http://127.0.0.1:8000'