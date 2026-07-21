from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path(
        '', include('homework29.urls')
    ),  # Подключаем все URL из вашего приложения
]