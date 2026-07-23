from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Стандартный вход/выход от Django, чтобы кнопка входа работала
    path(
        'accounts/', include('django.contrib.auth.urls')
    ),  # Предоставляет /accounts/login/
    path('', include('fitness.urls')),
]