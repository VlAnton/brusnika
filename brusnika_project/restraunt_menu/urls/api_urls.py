from django.urls import path
from rest_framework import routers

from . import api_views


router = routers.DefaultRouter()
router.register('languages', api_views.MenuItemViewset)

urlpatterns = [

]
