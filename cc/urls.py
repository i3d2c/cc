from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('api/', include('backendapi.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
