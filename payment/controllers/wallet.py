from django.http import JsonResponse
import json

from ..daos.wallet import WalletDAO


def get(request, user_id):
    if request.method == 'GET':
        info = WalletDAO.get_info_by_user_id(user_id)
        if info:
            return JsonResponse(info)


def create(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user_id = body.get('user_id')
        wallet = WalletDAO.create(user_id=user_id)
        if wallet:
            return JsonResponse(wallet)
