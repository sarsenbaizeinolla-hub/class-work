from django.contrib import admin
from django.urls import path, include
from homework29.views import index, booking_list, register, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Главная страница
    path('', index, name='index'),
    
    # Регистрация и авторизация
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Система бронирования
    path('bookings/', booking_list, name='booking_list'),
    
    # Если остались другие приложения, они остаются как есть:
    path('portfolio/', include('portfolio.urls')),
]
