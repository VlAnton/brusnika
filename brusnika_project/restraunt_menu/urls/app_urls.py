from django.urls import path, include, re_path
from ..views.app_views import MenuView


urlpatterns = [
    path('list/', MenuView.as_view())
]
