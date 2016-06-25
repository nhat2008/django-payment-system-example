from django.conf.urls import url

from controllers import withdraw
from controllers import deposit
from controllers import wallet

urlpatterns = [
    url(r'^deposit', deposit.create, name='create_deposit'),
    url(r'^withdraw', withdraw.create, name='create_withdraw'),
    url(r'^transfer', withdraw.transfer, name='create_transfer'),
    url(r'^wallet/(?P<user_id>\d+)', wallet.get, name='get_info'),
    url(r'^wallet/create', wallet.create, name='create_wallet'),
]
