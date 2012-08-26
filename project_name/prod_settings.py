import os, dj_database_url

PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = TEMPLATE_DEBUG = False


#SSL
# SESSION_COOKIE_SECURE = True
# SECURE_SSL_REDIRECT = True
# SESSION_COOKIE_HTTPONLY = True
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
# AWS_S3_SECURE_URLS = True

#PREPEND_WWW = True

MEDIA_ROOT = MEDIA_URL = ''

#S3
DEFAULT_FILE_STORAGE = STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = ''
STATIC_URL = '//%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
AWS_QUERYSTRING_AUTH = False


DOMAIN = ''


#db
DATABASES = { 'default': dj_database_url.config() }