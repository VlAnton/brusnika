from django.urls import path, include

from rest_framework import routers

from . import api_views


router = routers.DefaultRouter()

urlpatterns = [
    path('menu_items/', api_views.MenuAPIView.as_view(), name='menu')
]
