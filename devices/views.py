from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework import status
from .models import Device
from homes.models import Home


@api_view(['POST'])
@permission_classes([AllowAny])
def verify_device(request):
    print("VERIFY DEVICE HIT")  # <--- ต้องขึ้น
    print(request.data)
    device_id = request.data.get('device_id')

    if not device_id:
        return Response(
            {"error": "device_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        device = Device.objects.get(device_id=device_id)
    except Device.DoesNotExist:
        return Response(
            {
                "valid": False,
                "message": "Device not found"
            },
            status=status.HTTP_404_NOT_FOUND
        )

    return Response({
        "valid": True,
        "device_id": device.device_id,
        "model": device.model,
        "firmware": device.firmware,
        "claimed": device.owner is not None,
        "status": device.status
    })

@api_view(['POST'])
def claim_device(request):
    device_id = request.data.get('device_id')
    user = request.user

    if not device_id:
        return Response(
            {"error": "device_id is required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        device = Device.objects.get(device_id=device_id)
    except Device.DoesNotExist:
        return Response(
            {"error": "Device not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    if device.owner is not None:
        return Response(
            {"error": "Device already claimed"},
            status=status.HTTP_409_CONFLICT
        )

    device.owner = user
    device.status = 'claimed'
    device.save()

    return Response({
        "success": True,
        "device_id": device.device_id,
        "owner": user.username,
        "status": device.status
    })

@api_view(['POST'])
def assign_device_home(request):

    device_id = request.data.get("device_id")
    home_id = request.data.get("home_id")

    try:
        device = Device.objects.get(device_id=device_id)
        home = Home.objects.get(id=home_id)

    except:
        return Response(
            {"error": "Not found"},
            status=status.HTTP_404_NOT_FOUND
        )

    device.home = home
    device.save()

    return Response({"success": True})