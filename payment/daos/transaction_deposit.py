from django.utils import timezone
from ..models.transaction_deposit import TransactionDeposit


class TransactionDepositDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        # Pay loan first by using @LoanDAO.pay_decorate
        amount = kwargs['amount']
        wallet_id = kwargs['wallet_id']
        note = kwargs['note']
        withdraw_id = kwargs['withdraw_id']
        if amount > 0:
            deposit_trans = TransactionDeposit(wallet_id=wallet_id, amount=amount,
                                               note=note, status=TransactionDeposit.STATUS_ACTIVE,
                                               created_date=timezone.now(), withdraw_id=withdraw_id)
            deposit_trans.save()
            return deposit_trans

    @staticmethod
    def deposit_decorator(func):

        def func_wrapper(*args, **kwargs):
            deposit_transaction = TransactionDepositDAO.create(*args, **kwargs)
            kwargs['transaction'] = deposit_transaction
            return func(*args, **kwargs)
        return func_wrapper


