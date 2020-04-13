from django.urls import path

from restraunt_menu.api.views import MenuAPIView


app_name = 'api'

urlpatterns = [
    path('', MenuAPIView.as_view(), name='menu_items')
]
