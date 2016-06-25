from django.http import JsonResponse
from django.utils import timezone
import json
from django.db import transaction

from ..models.wallet import Wallet
from ..daos.wallet import WalletDAO


@transaction.atomic
def create(request):
    if request.method == 'POST':
        result = False
        body = json.loads(request.body)
        user_id = body.get('user_id')
        amount = body.get('amount')
        note = body.get('note')
        wallet = Wallet.objects.get(user_id=user_id)
        if wallet and amount > 0 and note:
            WalletDAO.add(wallet_id=wallet.id, amount=amount, note=note,
                          created_date=timezone.now(), withdraw_id=None)
            result = True
        return JsonResponse({'result': result})
