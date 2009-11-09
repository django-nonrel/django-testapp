from app.models import FieldsWithOptionsModel
import datetime
from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


class NonReturnSetsTest(TestCase):
    floats = [5.3, 2.6, 9.1, 1.58, 2.4]
    emails = ['app-engine@scholardocs.com', 'sharingan@uchias.com',
        'rinnengan@sage.de', 'rasengan@naruto.com', 'itachi@uchia.com']

    def setUp(self):
        for float, email in zip(NonReturnSetsTest.floats, NonReturnSetsTest.emails):
            model = FieldsWithOptionsModel(floating_point=float,
                                           integer=int(float), email=email,
                                           time=datetime.datetime.now().time())
            model.save()

    def test_get(self):
        self.assertEquals(FieldsWithOptionsModel.objects.get(
                                                email='itachi@uchia.com')
                                                .email, 'itachi@uchia.com')

        # test exception when matching multiple entities
        self.assertRaises(MultipleObjectsReturned, FieldsWithOptionsModel.objects
                            .get, integer=2)

        # test exception when entity does not exist
        self.assertRaises(ObjectDoesNotExist, FieldsWithOptionsModel.objects
                            .get, floating_point=5.2)

        # TODO: test create when djangos model.save_base is refactored
        # TODO: test get_or_create when refactored

    def test_count(self):
        self.assertEquals(FieldsWithOptionsModel.objects.filter(
            integer=2).count(), 2)

    def test_in_bulk(self):
        self.assertEquals([key in ['sharingan@uchias.com', 'itachi@uchia.com']
                        for key in FieldsWithOptionsModel.objects.in_bulk(
                                ['sharingan@uchias.com', 'itachi@uchia.com']).keys()],
                                [True, ]*2)

    def test_latest(self):
        self.assertEquals('itachi@uchia.com', FieldsWithOptionsModel.objects
            .latest('time').email)

    def test_exists(self):
        self.assertEquals(True, FieldsWithOptionsModel.objects.exists())

    def test_deletion(self):
        self.assertEquals(FieldsWithOptionsModel.objects.count(), 5)

        FieldsWithOptionsModel.objects.get(email='itachi@uchia.com').delete()
        self.assertEquals(FieldsWithOptionsModel.objects.count(), 4)

        FieldsWithOptionsModel.objects.filter(email__in=['sharingan@uchias.com',
            'itachi@uchia.com', 'rasengan@naruto.com', ]).delete()
        self.assertEquals(FieldsWithOptionsModel.objects.count(), 2)