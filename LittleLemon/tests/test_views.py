from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from Restaurant.views import *
from Restaurant.models import *
from Restaurant.serializers import *

class MenuViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password123')  # Create a test user
        self.token = Token.objects.create(user=self.user)  # Generate the token for the test user

        self.item1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=10)
        self.item2 = MenuItem.objects.create(title="Burger", price=8.99, inventory=15)
        self.item3 = MenuItem.objects.create(title="Pasta", price=10.00, inventory=7)
        
        self.client = APIClient()  # Use Django REST framework's API client
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)  # Add the token to the request headers

        
    def test_getall(self):
        response = self.client.get(reverse('menu-items'))
        
        menus = MenuItem.objects.all()
        expected_data = menuItemSerializer(menus, many=True).data

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Check for HTTP 200
        self.assertEqual(response.json(), expected_data)  # Ensure response matches serialized data

        