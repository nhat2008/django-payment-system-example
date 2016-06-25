from django.test import TestCase
from django.utils import timezone
from models.customer import Customer


class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="A", phone="0938166112", email="nminhnhat2008@gmail.com",
                                status=Customer.STATUS_ACTIVE, gender=Customer.GENDER_MEN,
                                created_date=timezone.now(), updated_date=timezone.now())

    def test_customer_phone(self):
        customer = Customer.objects.get(name="A")
        self.assertEqual(customer.phone, '0938166112')

    def test_customer_email(self):
        customer = Customer.objects.get(name="A")
        self.assertEqual(customer.email, 'nminhnhat2008@gmail.com')

    def test_customer_status(self):
        customer = Customer.objects.get(name="A")
        self.assertEqual(customer.status, Customer.STATUS_ACTIVE)

    def test_customer_gender(self):
        customer = Customer.objects.get(name="A")
        self.assertEqual(customer.gender, Customer.GENDER_MEN)


