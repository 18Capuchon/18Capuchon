from django.urls import path
from .views import verify_device, claim_device, assign_device_home, device_online

urlpatterns = [
    path('verify', verify_device),
    path('claim', claim_device),
    path('assign-home', assign_device_home),
    path('devices/online', device_online),
]
