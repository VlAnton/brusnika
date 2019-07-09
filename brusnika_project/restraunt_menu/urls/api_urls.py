from django.urls import path, include
from rest_framework import routers

from . import api_views


router = routers.DefaultRouter()
router.register('restraunt_menu', api_views.MenuItemViewset)

urlpatterns = [
    path('', include(router.urls))
]
