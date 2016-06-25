from __future__ import unicode_literals
from django.db import models
from wallet import Wallet
from transaction_withdraw import TransactionWithdraw
from django.utils.encoding import python_2_unicode_compatible
from concurrency.fields import IntegerVersionField


@python_2_unicode_compatible
class Loan(models.Model):
    # Cons value
    STATUS_ACTIVE = 1
    STATUS_DEACTIVE = 0
    STATUS = ((STATUS_ACTIVE, 'Active'),
              (STATUS_DEACTIVE, 'Deactive'))
    # Properties
    version = IntegerVersionField()
    wallet_debit = models.ForeignKey(Wallet, default=None, null=True, related_name='wallet_debit')
    wallet_credit = models.ForeignKey(Wallet, default=None, null=True, related_name='wallet_credit')
    transaction = models.OneToOneField(TransactionWithdraw, default=None, null=True)
    amount = models.FloatField(max_length=15, default=0.0)
    status = models.IntegerField(choices=STATUS, default=STATUS_ACTIVE)
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return "%s - Loan from - %s" % (self.wallet_debit.user.name, self.wallet_credit.user.name)
