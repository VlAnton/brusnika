from django.urls import path, include, re_path
from .app_views import MenuView, OrderView


urlpatterns = [
    path('list/', MenuView.as_view(), name='menu-app'),
    path('bill/', OrderView.as_view())
]
