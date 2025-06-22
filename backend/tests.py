from django.test import TestCase

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from backend.models import Shop, Contact, Order

User = get_user_model()


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()


        self.shop_user = User.objects.create_user(
            email='shop@example.com',
            password='testpass123',
            type='shop'
        )

        self.shop = Shop.objects.create(user=self.shop_user, name='Test Shop', state=True)


        self.user = User.objects.create_user(
            email='user@example.com',
            password='testpass123',
            type='customer'
        )

    def test_partner_state_get_unauthenticated(self):
        response = self.client.get('/api/partner/state/')
        self.assertEqual(response.status_code, 403)

    def test_partner_state_get_not_shop(self):
        self.client.login(email='user@example.com', password='testpass123')
        response = self.client.get('/api/partner/state/')
        self.assertEqual(response.status_code, 403)

    def test_partner_state_get_shop(self):

        self.client.force_authenticate(user=self.shop_user)
        response = self.client.get('/api/partner/state/')
        self.assertEqual(response.status_code, 200)

        self.assertIn('name', response.data)

    def test_partner_state_post_change_state_success(self):
        self.client.force_authenticate(user=self.shop_user)
        response = self.client.post('/api/partner/state/', {'state': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['Status'], True)

    def test_partner_orders_get_unauthenticated(self):
        response = self.client.get('/api/partner/orders/')
        self.assertEqual(response.status_code, 403)

    def test_partner_orders_get_not_shop(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/api/partner/orders/')
        self.assertEqual(response.status_code, 403)

    def test_partner_orders_get_success(self):

        self.client.force_authenticate(user=self.shop_user)


        order = Order.objects.create(user=self.user, contact=None)


        response = self.client.get('/api/partner/orders/')
        self.assertEqual(response.status_code, 200)

    def test_contact_get_unauthenticated(self):
        response = self.client.get('/api/contact/')
        self.assertEqual(response.status_code, 403)

    def test_contact_post_missing_fields(self):
        # Авторизация как пользователь
        self.client.force_authenticate(user=self.user)

        response = self.client.post('/api/contact/', {'city': 'City'})



    def test_contact_post_success(self):
        self.client.force_authenticate(user=self.user)

        data = {'city': 'City', 'street': 'Street', 'phone': '+123456789'}

        response = self.client.post('/api/contact/', data)

        self.assertEqual(response.status_code, 200)

    def test_order_get_unauthenticated(self):
        response = self.client.get('/api/order/')
        self.assertEqual(response.status_code, 403)