from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from concurrency.fields import IntegerVersionField


@python_2_unicode_compatible
class Customer(models.Model):
    GENDER_MEN = 1
    GENDER_WOMAN = 0
    GENDERS = (
        (GENDER_MEN, 'Men'),
        (GENDER_WOMAN, 'Woman')
    )
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 1
    STATUS = ((STATUS_ACTIVE, 'Active'),
              (STATUS_DEACTIVE, 'Deactive'))
    # encrypted_id = models.CharField(max_length=32)
    version = IntegerVersionField()
    name = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    email = models.CharField(max_length=256)
    number = models.CharField(max_length=15)
    status = models.IntegerField(choices=STATUS, default=STATUS_ACTIVE)
    gender = models.IntegerField(choices=GENDERS, default=GENDER_MEN)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
