from app.models import FieldsWithOptionsModel
from django.test import TestCase
import datetime

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

    def test_gt(self):
        self.assertEquals([entity.floating_point for entity in \
                            FieldsWithOptionsModel.objects.filter(
                            floating_point__gt=3).order_by('floating_point')],
                            [5.3, 9.1])

        self.assertEquals([entity.email for entity in \
                            FieldsWithOptionsModel.objects.filter(email__gt='as').
                            order_by('email')], ['rasengan@naruto.com',
                            'rinnengan@sage.de', 'sharingan@uchias.com', ])

    def test_lt(self):
        pass

    def test_gte(self):
        pass

    def test_lte(self):
        pass

    def test_multi_filter(self):
        pass

    def test_exclude(self):
        pass

    # pk_in is tested in order.py
#    def test_pk_in(self):
#        pass