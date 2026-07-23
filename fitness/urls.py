from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='fitness/login.html'),
        name='login',
    ),
    path(
        'logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'
    ),
    path('trainers/', views.trainers_view, name='trainers'),
    path('subscriptions/', views.subscriptions_view, name='subscriptions'),
    path('buy/<int:sub_id>/', views.buy_subscription, name='buy_subscription'),
    path('booking/', views.booking_view, name='booking'),
    path('profile/', views.profile_view, name='profile'),
]