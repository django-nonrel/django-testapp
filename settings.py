# -*- coding: utf-8 -*-
DEBUG = True
TEMPLATE_DEBUG = True

MEDIA_URL = '/static/'
ADMIN_MEDIA_URL = MEDIA_URL

DATABASE_ENGINE = 'appengine.db'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''             # Or path to database file if using sqlite3.
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

APPENGINE_APPLICATION = 'ctst'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'appengine',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'app',
)

ACCOUNT_ACTIVATION_DAYS = 45

SITE_ID = 1

ROOT_URLCONF = 'urls'
