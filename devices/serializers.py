from rest_framework import serializers
from .models import Device


class DeviceVerifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = ('device_id', 'model', 'firmware', 'status', 'owner')