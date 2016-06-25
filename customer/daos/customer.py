from __builtin__ import staticmethod

from ..models.customer import Customer


class CustomerDAO(object):
    def __init__(self):
        pass

    @staticmethod
    def get_info_by_user_id(user_id):
        user = Customer.objects.get(id=user_id)
        if user:
            result = {}
            result['name'] = user.name
            result['phone'] = user.phone
            result['email'] = user.version
            result['number'] = user.number
            result['status'] = user.status
            result['gender'] = user.gender
            return result
        return False

    @staticmethod
    def create(*args, **kwargs):
        result = {}
        try:
            name = kwargs['name']
            phone = kwargs['phone']
            email = kwargs['email']
            number = kwargs['number']
            gender = kwargs['gender']
            customer = Customer(name=name, phone=phone, email=email, number=number, gender=gender)
            customer.save()
            result['result'] = True
            result['id'] = customer.id
        except Exception as e:
            result['result'] = False
        return result
