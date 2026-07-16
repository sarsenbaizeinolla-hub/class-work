from django.contrib import admin
from django.urls import path, include
from homework29.views import index, register, login_view # Здесь мы импортируем все три
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('portfolio/', include('portfolio.urls')),
    path('login/', login_view, name='login'), # Теперь этот путь будет работать
    path('register/', register, name='register'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]