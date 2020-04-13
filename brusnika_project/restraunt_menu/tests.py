from django.shortcuts import reverse

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Allergens, Category, MenuItem


class AccountTests(APITestCase):
    def test_add(self):
        url = reverse('menu')
        data = {
            'title': 'test menu item',
            'calories': '228kkal',
            'price': 228
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_add_without_price_or_title(self):
        url = reverse('menu')
        data_1 = {
            'title': 'test menu item',
            'calories': '228kkal',
        }
        response_1 = self.client.post(url, data_1, format='json')

        data_2 = {
            'calories': '228kkal',
            'price': 228
        }
        response_2 = self.client.post(url, data_2, format='json')

        self.assertEqual(response_1.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_correct_foreign_key_handling(self):
        url = reverse('menu')
        data = {
            'title': 'test menu item',
            'calories': '228kkal',
            'price': 228,
            'list_of_allergens': 'nuts, eggs, tomatoes',
            'category': 'fat'
        }
        response = self.client.post(url, data, format='json')

        instance = MenuItem.objects.get(title=data['title'])
        allergens = Allergens.objects.get(list_of_allergens=data['list_of_allergens'])
        category = Category.objects.get(name=data['category'])

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNotEqual(instance, None)
        self.assertNotEqual(allergens, None)
        self.assertNotEqual(category, None)
