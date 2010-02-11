from djangoappengine.settings_base import *

SECRET_KEY = '=r-$b*8hglm+858&9t043hlm6-&6-3d3vfc4((7yd0dbrakhvi'

INSTALLED_APPS = (
    'djangoappengine',
#    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
)

ADMIN_MEDIA_PREFIX = '/media/admin/'

import os
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)
