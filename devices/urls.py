from django.urls import path
from .views import verify_device, claim_device, create_home, list_home, assign_device_home

urlpatterns = [
    path('verify', verify_device),
    path('claim', claim_device),
    path('assign-home', assign_device_home),
]
