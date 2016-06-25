from __future__ import unicode_literals
from django.db import models
from customer.models.customer import Customer
from django.utils.encoding import python_2_unicode_compatible
from concurrency.fields import IntegerVersionField


@python_2_unicode_compatible
class Wallet(models.Model):
    version = IntegerVersionField()
    user = models.OneToOneField(Customer)
    amount = models.FloatField(max_length=15, default=0.0)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s - Wallet" % (self.user.name,)
