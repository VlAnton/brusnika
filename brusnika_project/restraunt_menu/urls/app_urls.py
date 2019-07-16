from django.urls import path, include, re_path
from ..views.app_views import MenuView, OrderView


urlpatterns = [
    path('list/', MenuView.as_view()),
    path('bill/', OrderView.as_view())
]
