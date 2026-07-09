from django.urls import path
from . import views

urlpatterns = [
    path('', views.AdListView.as_view(), name='ads_list'),
    path('ad/<int:pk>/', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/new/', views.AdCreateView.as_view(), name='ad_create'),
    path('ad/<int:pk>/delete/', views.AdDeleteView.as_view(), name='ad_delete'),
]