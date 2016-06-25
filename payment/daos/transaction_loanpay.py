from django.utils import timezone
from ..models.transaction_loanpay import TransactionLoanPay


class TransactionLoanPayDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        amount = kwargs['amount']
        note = kwargs['note']
        loan_id = kwargs['loan_id']
        if amount > 0:
            loanpay_trans = TransactionLoanPay(wallet_id=wallet_id, amount=amount,
                                               note=note, status=TransactionLoanPay.STATUS_ACTIVE,
                                               created_date=timezone.now(), loan_id=loan_id)
            loanpay_trans.save()
            return loanpay_trans

    @staticmethod
    def loanpay_decorator(func):
        def func_wrapper(*args, **kwargs):
            loanpay_trans = TransactionLoanPayDAO.create(*args, **kwargs)
            kwargs['transaction'] = loanpay_trans
            return func(*args, **kwargs)
        return func_wrapper
