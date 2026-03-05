from django.urls import path
from .views import verify_device, claim_device

urlpatterns = [
    path('verify', verify_device),
    path('claim', claim_device),

    path('home/create', create_home),
    path('home/list', list_home),

    path('device/assign-home', assign_device_home),
]
