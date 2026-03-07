from django.urls import path
from .views import create_home, list_home

urlpatterns = [
    path('create/', create_home),
    path('', list_home),
]