from django.urls import path

from restraunt_menu.api.views import MenuAPIView


app_name = 'api'

urlpatterns = [
    path('menu_items/', MenuAPIView.as_view(), name='menu')
]
