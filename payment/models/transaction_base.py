from __future__ import unicode_literals
from django.db import models
from concurrency.fields import IntegerVersionField


class TransactionBase(models.Model):
    # Cons value
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 1
    STATUS = ((STATUS_ACTIVE, 'Active'),
              (STATUS_DEACTIVE, 'Deactive'))
    # Properties
    version = IntegerVersionField()
    wallet = models.ForeignKey('Wallet')
    amount = models.FloatField(max_length=15, default=0.0)
    note = models.CharField(max_length=256, default='')
    status = models.IntegerField(choices=STATUS, default=STATUS_ACTIVE)
    created_date = models.DateTimeField(blank=True, null=True)