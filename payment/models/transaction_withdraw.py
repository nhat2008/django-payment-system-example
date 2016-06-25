from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models

from transaction_base import TransactionBase


@python_2_unicode_compatible
class TransactionWithdraw(TransactionBase):
    def __str__(self):
        return "%s - Withdraw Transaction - %d" % (self.wallet.user.name, self.id)


