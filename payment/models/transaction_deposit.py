from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from transaction_base import TransactionBase
from transaction_withdraw import TransactionWithdraw


@python_2_unicode_compatible
class TransactionDeposit(TransactionBase):
    withdraw = models.ForeignKey(TransactionWithdraw, default=None, null=True)

    def __str__(self):
        return "%s - Deposit Transaction - %d" % (self.wallet.user.name, self.id)

