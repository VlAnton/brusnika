from django.urls import path, include

from rest_framework import routers

from . import api_views


router = routers.DefaultRouter()
router.register('menu_items', api_views.MenuItemViewset, base_name='menu')
router.register('categories', api_views.CategoryViewSet)
router.register('allergens', api_views.AllergensViewSet)

urlpatterns = [
    path('', include(router.urls), name='menu'),
]
