from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('register/', views.register_view, name='register'),
    path('trainers/', views.trainers_view, name='trainers'),
    path('subscriptions/', views.subscriptions_view, name='subscriptions'),
    path('buy/<int:sub_id>/', views.buy_subscription, name='buy_subscription'),
    path('booking/', views.booking_view, name='booking'),
    path('profile/', views.profile_view, name='profile'),
]