from django.utils import timezone
from django.db.models import Sum
# Local Project
from ..models.wallet import Wallet
from ..models.loan import Loan
from ..models.transaction_loanpay import TransactionLoanPay
from ..models.transaction_withdraw import TransactionWithdraw


class LoanDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def create(*args, **kwargs):
        wallet_debit_id = kwargs['wallet_debit_id']
        wallet_credit_id = kwargs['wallet_credit_id']
        amount = kwargs['amount']
        transaction_id = kwargs['transaction_id']
        if amount > 0:
            loan = Loan(wallet_debit_id=wallet_debit_id, wallet_credit_id=wallet_credit_id,
                        amount=amount, transaction_id=transaction_id,
                        status=Loan.STATUS_ACTIVE, created_date=timezone.now(),
                        updated_date=timezone.now())
            loan.save()
            return loan
        return False

    @staticmethod
    def check_existing(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        if Loan.objects.filter(wallet_debit_id=wallet_id).exists():
            return True
        return False

    @staticmethod
    def get_total_money(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        loans = Loan.objects.filter(wallet_debit_id=wallet_id).order_by('created_date')
        loan_money = 0
        for loan in loans:
            loan_money += LoanDAO.get_needing_pay(amount=loan.amount, loan_id=loan.id)
        return loan_money or 0

    @staticmethod
    def get_needing_pay(*args, **kwargs):
        loan_id = kwargs['loan_id']
        amount = kwargs['amount']
        total_payment = TransactionLoanPay.objects.filter\
                                            (loan_id=loan_id).\
                                            aggregate(Sum('amount'))['amount__sum']
        total_payment = total_payment or 0
        rest_payment = amount - total_payment
        return max(rest_payment, 0)

    @staticmethod
    def pay(*args, **kwargs):
        wallet_id = kwargs['wallet_id']
        note_payment = "Payment from a borrower"
        note_payloan = "Pay loan"
        wallet = Wallet.objects.get(id=wallet_id)
        amount = wallet.amount
        loans = Loan.objects.filter(wallet_debit_id=wallet_id).order_by('created_date')
        for loan in loans:
            if amount > 0:
                needing_pay_amount = LoanDAO.get_needing_pay(amount=loan.amount, loan_id=loan.id)
                if needing_pay_amount > 0 and amount > 0:
                    paying_amount = min(amount, needing_pay_amount)
                    from ..daos.wallet import WalletDAO
                    # Decrease Wallet Debit
                    trans_minus = WalletDAO.minus(wallet_id=loan.wallet_debit.id, amount=paying_amount,
                                                  note=note_payloan, status=TransactionWithdraw.STATUS_ACTIVE,
                                                  created_date=timezone.now())
                    # Increase Wallet Credit
                    trans_add = WalletDAO.add(wallet_id=loan.wallet_credit.id, amount=paying_amount,
                                              note=note_payment, created_date=timezone.now(),
                                              withdraw_id=None)
                    # Create Transaction Loan
                    transaction_loanpay = TransactionLoanPay(wallet_id=wallet_id, amount=paying_amount,
                                                             note=note_payloan, status=Loan.STATUS_ACTIVE,
                                                             created_date=timezone.now(), loan_id=loan.id)
                    transaction_loanpay.save()

                    # Check if pay all for the current loan
                    if amount >= needing_pay_amount:
                        loan.status = Loan.STATUS_DEACTIVE
                        loan.save()
                    # Update input amount after paying money
                    amount -= needing_pay_amount
        return amount

    @staticmethod
    def pay_decorator(func):
        def func_wrapper(*args, **kwargs):
            amount = LoanDAO.pay(*args, **kwargs)
            kwargs['amount'] = amount
            return func(*args, **kwargs)
        return func_wrapper
