from django.shortcuts import render
from rest_framework import viewsets

from ..models import (MenuItem, Allergens, Category)
from ..serializers import (
    MenuItemSerializer,
    AllergensSerializer,
    CategorySerializer
)


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.items.all()
    serializer_class = MenuItemSerializer


class AllergensViewSet(viewsets.ModelViewSet):
    queryset = Allergens.objects.all()
    serializer_class = AllergensSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


