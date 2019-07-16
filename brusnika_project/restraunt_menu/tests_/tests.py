from django.shortcuts import reverse

from rest_framework import status
from rest_framework.test import APITestCase


# class AccountTests(APITestCase):
#     def test_add_to_menu(self):
#         url = reverse('menu-list')
#         data = {
#             'title': 'test menu item',
#             'calories': '228kkal',
#             'price': 228
#         }
#         response = self.client.post(url, data, format='json')

#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
