from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response

from ..models import (MenuItem, Allergens, Category)
from ..serializers import (
    MenuItemSerializer,
    AllergensSerializer,
    CategorySerializer
)


class MenuItemViewset(viewsets.ModelViewSet):
    queryset = MenuItem.items.all()
    serializer_class = MenuItemSerializer

class MenuAPIView(APIView):
    def get(self, request):
        menu_items = MenuItem.items.all() 
        serializer = MenuItemSerializer(menu_items, many=True)

        return Response(serializer.data)

    def post(self, request):
        pass

class AllergensViewSet(viewsets.ModelViewSet):
    queryset = Allergens.alergens.all()
    serializer_class = AllergensSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.categories.all()
    serializer_class = CategorySerializer


