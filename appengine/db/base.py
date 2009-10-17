"""
App Engine backend for Django.

Python module google.appengine is required (either from SDK or the one
available in production envrionment).

Some parts of this code are derived from the App Engine Helper:
http://code.google.com/p/google-app-engine-django/
"""

from common.appenginepatch.aecmd import setup_env
setup_env()

from django.conf import settings
from django.db.backends import (
    BaseDatabaseFeatures,
    BaseDatabaseOperations,
    BaseDatabaseWrapper,
    )
from appengine.db.creation import DatabaseCreation

try:
    import google.appengine.ext.db
except ImportError, err:
    from django.core.exceptions import ImproperlyConfigured
    raise ImproperlyConfigured, "App Engine module is required (%s)." % err

from google.appengine.tools import dev_appserver

from appengine import util


DatabaseError = google.appengine.ext.db.Error
IntegrityError = google.appengine.ext.db.Error


def get_datastore_paths(with_test=False):
    """Returns a tuple with the path to the datastore and history file.

    The datastore is stored in the same location as dev_appserver uses by
    default, but the name is altered using either settings.DATABASE_NAME
    or if this isn't set the app_id.

    Returns:
      (datastore_path, history_path)
    """
    # Note: dev_appserver_main can not be imported on module level.
    # dev_appserver_main's decorators will fail if it's imported too
    # early.
    from google.appengine.tools import dev_appserver_main
    datastore_path = dev_appserver_main.DEFAULT_ARGS['datastore_path']
    history_path = dev_appserver_main.DEFAULT_ARGS['history_path']
    fragment = settings.DATABASE_NAME or util.get_appid()
    if with_test:
        fragment = 'test_%s' % fragment
    datastore_path = datastore_path.replace('dev_appserver',
                                            'django_%s' % fragment)
    history_path = history_path.replace('dev_appserver',
                                        'django_%s' % fragment)
    return datastore_path, history_path


def get_test_datastore_paths(inmemory=True):
    """Returns a tuple with the path to the test datastore and history file.

    If inmemory is true, (None, None) is returned to request an in-memory
    datastore. If inmemory is false the path returned will be similar to
    the path returned by get_datastore_paths but with a different name.

    Returns:
      (datastore_path, history_path)
      """
    if inmemory:
        return None, None
    return get_datastore_paths(with_test=True)


class DatabaseFeatures(BaseDatabaseFeatures):
    pass

class DatabaseOperations(BaseDatabaseOperations):
    pass

class DatabaseWrapper(BaseDatabaseWrapper):

    def __init__(self, *args, **kwds):
        super(DatabaseWrapper, self).__init__(*args, **kwds)
        self.features = DatabaseFeatures()
        self.ops = DatabaseOperations()
        self.creation = DatabaseCreation(self)
        self.use_test_datastore = kwds.get("use_test_datastore", False)
        self.test_datastore_inmemory = kwds.get("test_datastore_inmemory",
                                                True)
        if not util.have_appserver():
            self._setup_stubs()

    def _get_paths(self):
        if self.use_test_datastore:
            return get_test_datastore_paths(self.test_datastore_inmemory)
        else:
            return get_datastore_paths()

    def _setup_stubs(self):
        # If this code is being run without an appserver (eg. via a django
        # commandline flag) then setup a default stub environment.
        from google.appengine.tools import dev_appserver_main
        args = dev_appserver_main.DEFAULT_ARGS.copy()
        args['datastore_path'], args['history_path'] = self._get_paths()
        dev_appserver.SetupStubs(util.get_appid(), **args)
