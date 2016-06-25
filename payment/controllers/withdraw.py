from django.http import JsonResponse
from django.utils import timezone
from django.db import transaction
import json

from ..models.wallet import Wallet
from ..daos.wallet import WalletDAO
from ..daos.loan import LoanDAO
from ..models.transaction_withdraw import TransactionWithdraw


@transaction.atomic
def create(request):
    if request.method == 'POST':
        result = False
        body = json.loads(request.body)
        user_id = body.get('user_id')
        wallet = Wallet.objects.get(user_id=user_id)
        amount = body.get('amount')
        note = body.get('note')

        if wallet and amount and note:
            WalletDAO.minus(wallet_id=wallet.id, amount=amount, note=note,
                            status=TransactionWithdraw.STATUS_ACTIVE,
                            created_date=timezone.now())
            result = True
    return JsonResponse({'result': result})


@transaction.atomic
def transfer(request):
    body = json.loads(request.body)
    user_id = body.get('user_id')
    wallet = Wallet.objects.get(user_id=user_id)
    amount = body.get('amount')
    note = body.get('note')
    destination_id = body.get('destination_id')
    wallet_des = Wallet.objects.get(user_id=destination_id)

    if amount and note:
        trans_minus = WalletDAO.minus(wallet_id=wallet.id, amount=amount,
                                      note=note, status=TransactionWithdraw.STATUS_ACTIVE,
                                      created_date=timezone.now())
        trans_add = WalletDAO.add(wallet_id=wallet_des.id, amount=amount,
                                  note=note, created_date=timezone.now(),
                                  withdraw_id=trans_minus.id)
        loan = LoanDAO.create(wallet_credit_id=wallet.id, wallet_debit_id=wallet_des.id,
                              transaction_id=trans_minus.id, amount=amount)
        result = True
    return JsonResponse({'result': result})

