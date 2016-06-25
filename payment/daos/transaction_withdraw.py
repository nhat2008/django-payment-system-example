from django.utils import timezone
from ..models.transaction_withdraw import TransactionWithdraw


class TransactionWithdrawDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        amount = kwargs['amount']
        note = kwargs['note']
        if amount > 0:
            withdraw_trans = TransactionWithdraw(wallet_id=wallet_id, amount=amount,
                                                 note=note, status=TransactionWithdraw.STATUS_ACTIVE,
                                                 created_date=timezone.now())
            withdraw_trans.save()
            return withdraw_trans

    @staticmethod
    def withdraw_decorator(func):
        def func_wrapper(*args, **kwargs):
            withdraw_trans = TransactionWithdrawDAO.create(*args, **kwargs)
            kwargs['transaction'] = withdraw_trans
            return func(*args, **kwargs)
        return func_wrapper
