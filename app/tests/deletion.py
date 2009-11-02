from app.models import FieldsWithOptionsModel
import datetime
from django.test import TestCase
from google.appengine.api.datastore_errors import BadArgumentError, BadFilterError

class FilterTest(TestCase):
    floats = [5.3, 2.6, 9.1, 1.58]
    emails = ['app-engine@scholardocs.com', 'sharingan@uchias.com',
        'rinnengan@sage.de', 'rasengan@naruto.com']

    def setUp(self):
        for float, email in zip(FilterTest.floats, FilterTest.emails):
            model = FieldsWithOptionsModel(floating_point=float,
                                           integer=int(float), email=email,
                                           time=datetime.datetime.now().time())
            model.save()

    def test_deletion(self):
        # TODO: test deletion
        pass