from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('bookings/', views.booking_list, name='booking_list'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]