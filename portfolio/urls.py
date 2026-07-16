from django.urls import path
from .views import portfolio_view, delete_asset

urlpatterns = [
    path('', portfolio_view, name='portfolio'),
    path('delete/<int:pk>/', delete_asset, name='delete_asset'),
]