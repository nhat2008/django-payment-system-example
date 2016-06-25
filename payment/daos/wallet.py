from __builtin__ import staticmethod

from django.utils import timezone

from ..models.wallet import Wallet
from ..daos.transaction_deposit import TransactionDepositDAO
from ..daos.transaction_withdraw import TransactionWithdrawDAO
from ..daos.loan import LoanDAO
from customer.models.customer import Customer


class WalletDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        result = {}
        user_id = kwargs['user_id']
        wallet = Wallet.objects.filter(user_id=user_id)
        if wallet:
            result['wallet_id'] = wallet[0].id
        else:
            if Customer.objects.filter(id=user_id).exists():
                wallet = Wallet(user_id=user_id)
                wallet.save()
                result['wallet_id'] = wallet.id
        return result

    @staticmethod
    def get_info_by_user_id(user_id):
        wallet = Wallet.objects.get(user_id=user_id)
        if wallet:
            result = {}
            result['amount'] = wallet.amount
            result['loan'] = LoanDAO.get_total_money(wallet_id=wallet.id)
            return result
        return False


    @staticmethod
    @TransactionDepositDAO.deposit_decorator
    def add(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        amount = kwargs['amount']
        # This transaction will be returned by @decorator
        deposit_trans = kwargs['transaction']

        wallet = Wallet.objects.get(id=wallet_id)
        wallet.amount += amount
        wallet.updated_date = timezone.now()
        wallet.save()
        # Pay Money for each time add money
        if LoanDAO.check_existing(wallet_id=wallet_id):
            LoanDAO.pay(wallet_id=wallet_id)
        return deposit_trans

    @staticmethod
    @TransactionWithdrawDAO.withdraw_decorator
    def minus(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        amount = kwargs['amount']
        # This transaction will be returned by @decorator
        withdraw_trans = kwargs['transaction']

        wallet = Wallet.objects.get(id=wallet_id)
        wallet.amount -= amount
        wallet.updated_date = timezone.now()
        wallet.save()
        return withdraw_trans

    @staticmethod
    def check_add(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        amount = kwargs['amount']
        wallet = Wallet.objects.filter(wallet_debit_id=wallet_id, amount__gte=amount)
        if not wallet:
            return False
        return True
