from django.test import TestCase
from app.models import FieldsWithOptionsModel
from google.appengine.api.datastore import Get
from google.appengine.ext.db import Key
from google.appengine.api.datastore_types import Text, Category, Email, Link, \
    PhoneNumber, PostalAddress, Text, unicode, Blob, ByteString, GeoPt, IM, Key, \
    Rating, user.User, BlobKey, datetime.datetime


# TODO: Fix Djangos TimeField bug, it has to be value.time() instead of
# value.time
class FieldOptionsTest(TestCase):
    def testDBConvertion(self):
#        # first check if putting entities work
#        ModelFieldsWithoutOptions().save()
#        self.assertEqual(ModelFieldsWithoutOptions().objects.count(), 1)

        entity_with_options = FieldsWithOptionsModel()
        entity_with_options.save()
        self.assertEquals