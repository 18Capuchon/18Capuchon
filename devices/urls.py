from django.urls import path
from .views import verify_device, claim_device

urlpatterns = [
    path('verify', verify_device),
    path('claim', claim_device),
]
