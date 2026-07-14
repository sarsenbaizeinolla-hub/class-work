from django.urls import path
from . import views

urlpatterns = [
    path('', views.pr33_postgres_view, name='pr33_postgres'),
]