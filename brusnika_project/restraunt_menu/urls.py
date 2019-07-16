from django.urls import include, path

from .api import api_urls
from .app import app_urls


urlpatterns = [
    path('api/', include(api_urls)),
    path('app/', include(app_urls)),
]
