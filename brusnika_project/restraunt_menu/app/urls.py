from django.urls import path, include, re_path
from restraunt_menu.app.views import ListView, OrderView


app_name = 'app'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('bill/', OrderView.as_view(), name='bill')
]
