from django.conf.urls import url
from controllers import customer

urlpatterns = [
    url(r'^(?P<id>\d+)$', customer.get, name='get_user'),
    url(r'^create', customer.create, name='create_user'),

]
