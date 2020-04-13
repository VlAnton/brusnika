from django.contrib import admin
from django.urls import path, include

from restraunt_menu.app import urls as app_urls
from restraunt_menu.api import urls as api_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(app_urls)),
    path('api/', include(api_urls)),
]
