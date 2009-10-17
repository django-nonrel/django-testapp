"""Helper functions"""

import os

from django.conf import settings

from google.appengine.api import apiproxy_stub_map
from google.appengine.tools import dev_appserver

_appid = None
_have_appserver = None


def read_appid():
    """Return the application name.

    If the APPLICATION_ID environment variable is set (e.g. in production
    environment) it's read from the environment, otherwise it requires
    settings.APPENGINE_APPLICATION to bet configured.
    """
    # TODO(andi): What should we do with app.yaml? If this module is installed
    #   system-wide, we have no clue where to search app.yaml.
    if 'APPLICATION_ID' in os.environ:
        return os.environ['APPLICATION_ID']
    app_id = getattr(settings, 'APPENGINE_APPLICATION')
    if app_id is None:
        raise ImproperlyConfigured('settings.APPENGINE_APPLICATION is not set')
    return app_id


def get_appid():
    global _appid
    if _appid is None:
        _appid = read_appid()
    return _appid

def have_appserver():
    global _have_appserver
    if _have_appserver is None:
        stub = apiproxy_stub_map.apiproxy.GetStub("datastore_v3")
        if stub:
            _have_appserver = True
        else:
            _have_appserver = False
    return _have_appserver
