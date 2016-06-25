from django.contrib import admin
# Local Project
from models.wallet import Wallet
from models.transaction_deposit import TransactionDeposit
from models.transaction_withdraw import TransactionWithdraw
from models.loan import Loan
from models.transaction_loanpay import TransactionLoanPay
from models.transaction_base import TransactionBase


# Register your models here.
admin.site.register(Wallet)
admin.site.register(TransactionWithdraw)
admin.site.register(TransactionDeposit)
admin.site.register(Loan)
admin.site.register(TransactionLoanPay)
