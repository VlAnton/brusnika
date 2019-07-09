from django.shortcuts import render
from rest_framework import viewsets

from ..models import (MenuItem, AllergensModel, Category)
from ..serializers import MenuItemSerializer


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.items.all()
    serializer_class = MenuItemSerializer
