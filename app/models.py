from django.db import models
from django.utils.translation import ugettext_lazy as _

class FlatPage(models.Model):
    title = models.CharField(_('Title'), max_length=100, db_index=True)

#class FlatterPage(FlatPage):
#    url = models.CharField(_('url'), max_length=200)
#    content = models.TextField(_('content'), blank=True)

class Ptr(models.Model):
    page = models.ForeignKey(FlatPage, related_name='ptrs')
    title = models.CharField(_('Title'), max_length=200)
