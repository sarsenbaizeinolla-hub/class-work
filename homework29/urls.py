from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),      # Имя 'login' совпадает с base.html
    path('register/', views.register, name='register'),  # Имя 'register' совпадает с base.html
]