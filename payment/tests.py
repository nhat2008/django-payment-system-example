from django.test import TestCase
from django.utils import timezone
from models.wallet import Wallet
from customer.models.customer import Customer


class WalletTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="A", phone="0938166112", email="nminhnhat2008@gmail.com",
                                                status=Customer.STATUS_ACTIVE, gender=Customer.GENDER_MEN,
                                                created_date=timezone.now(), updated_date=timezone.now())
        Wallet.objects.create(user_id=self.customer.id, amount=0,
                              created_date=timezone.now(), updated_date=timezone.now())

    def test_wallet_customer(self):
        wallet = Wallet.objects.get(user_id=self.customer.id)
        self.assertEqual(wallet.user.id, self.customer.id)

    def test_wallet_amount(self):
        wallet = Wallet.objects.get(user_id=self.customer.id)
        self.assertEqual(wallet.amount, 0)


class WalletTestCase(TestCase):
    def setUp(self):
        self.customer = Customer.objects.create(name="A", phone="0938166112", email="nminhnhat2008@gmail.com",
                                                status=Customer.STATUS_ACTIVE, gender=Customer.GENDER_MEN,
                                                created_date=timezone.now(), updated_date=timezone.now())
        Wallet.objects.create(user_id=self.customer.id, amount=0,
                              created_date=timezone.now(), updated_date=timezone.now())

    def test_wallet_customer(self):
        wallet = Wallet.objects.get(user_id=self.customer.id)
        self.assertEqual(wallet.user.id, self.customer.id)

    def test_wallet_amount(self):
        wallet = Wallet.objects.get(user_id=self.customer.id)
        self.assertEqual(wallet.amount, 0)
