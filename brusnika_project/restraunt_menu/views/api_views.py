from django.shortcuts import render
from rest_framework import viewsets

from restraunt_menu.models import (MenuItem, AllergensModel, Category)
from restraunt_menu.serializers import MenuItemSerializer


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.items.all()
    serializer_class = MenuItemSerializer
