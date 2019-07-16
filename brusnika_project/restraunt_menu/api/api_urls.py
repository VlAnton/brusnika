from django.urls import path, include

from rest_framework import routers

from .api_views import MenuAPIView


router = routers.DefaultRouter()

urlpatterns = [
    path('menu_items/', MenuAPIView.as_view(), name='menu')
]
