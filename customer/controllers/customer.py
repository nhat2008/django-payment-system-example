from django.http import JsonResponse
from ..daos.customer import CustomerDAO
import json
# Create your controllers here.


def get(request, id):
    if request.method == 'GET':
        info = CustomerDAO.get_info_by_user_id(id)
        if info:
            return JsonResponse(info)


def create(request):
    body = json.loads(request.body)
    name = body.get('name', False)
    phone = body.get('phone', False)
    email = body.get('email', False)
    number = body.get('number', False)
    gender = body.get('gender', False)
    if name and phone and email and number and gender:
        customer = CustomerDAO.create(name=name, phone=phone, email=email, number=number, gender=gender)
        return JsonResponse(customer)
