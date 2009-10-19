from django.db import models
from django.utils.translation import ugettext_lazy as _

class FlatPage(models.Model):
    title = models.CharField(_('Title'), max_length=10, db_index=True)
    content = models.TextField(_('Content'))
    active = models.BooleanField(default=True)
    integer_list = models.CommaSeparatedIntegerField(max_length=20,
        default="10, 20, 5, 4")
    email = models.EmailField()
    velocity = models.FloatField()
    age = models.PositiveIntegerField()

#class FlatterPage(FlatPage):
#    url = models.CharField(_('url'), max_length=200)
#    content = models.TextField(_('content'), blank=True)

class Ptr(models.Model):
    page = models.ForeignKey(FlatPage, related_name='ptrs')
    title = models.CharField(_('Title'), max_length=200)

class ModelFieldsWithoutOptions(models.Model):
    datetime = models.DateTimeField()
    date = models.DateField()
    time = models.TimeField()
    floating_point = models.FloatField()
    boolean = models.BooleanField()
    null_boolean = models.NullBooleanField()
    text = models.CharField()
    email = models.EmailField()
#    comma_seperated_integer = models.CommaSeparatedIntegerField()
    ip_address = models.IPAddressField()
    slug = models.SlugField()
    url = models.URLField()
#    file = models.FileField()
#    file_path = models.FilePathField()
    long_text = models.TextField()
    xml = models.XMLField()
    integer = models.IntegerField()
    small_integer = models.SmallIntegerField()
    positiv_integer = models.PositiveIntegerField()
    positiv_small_integer = models.PositiveSmallIntegerField()
#    one_to_one = models.OneToOneField()
#    decimal = models.DecimalField() # can be None
#    image = models.ImageField()

class FieldsWithOptions(models.Model):
    # any type of unique is not supported on GAE, instead you can use
    # primary_key=True for some special cases. But be carefull: changing the
    # primary_key of an entity will not result an updated entity, instead a new
    # entity will be putted into the datastore. The old one will not be deleted
    # and all references pointing to the old entitiy will not point to the new one
    # either
    datetime = models.DateTimeField(auto_now=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField()
    floating_point = models.FloatField(null=True)
    boolean = models.BooleanField() # default is False
    null_boolean = models.NullBooleanField(default=True)
    text = models.CharField(default='Hallo', max_length=10)
    email = models.EmailField(default='gaga@gblabla.com', primary_key=True)
#    comma_seperated_integer = models.CommaSeparatedIntegerField()
    ip_address = models.IPAddressField(default="192.168.0.2")
    slug = models.SlugField(default="GAGAA")
    url = models.URLField(default='http://www.scholardocs.com')
#    file = FileField()
#    file_path = FilePathField()
    long_text = models.TextField(default=1000*'A')
    xml = models.XMLField(default=2000*'B')
    integer = models.IntegerField(default=100)
    small_integer = models.SmallIntegerField(default=-5)
    positiv_integer = models.PositiveIntegerField(default=80)
    positiv_small_integer = models.PositiveSmallIntegerField(default=3)
#    one_to_one = OneToOneField()
#    decimal = DecimalField()
#    image = ImageField()