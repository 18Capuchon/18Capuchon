from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):

    username = request.data.get("username")
    password = request.data.get("password")
    email = request.data.get("email")

    if not username or not password:
        return Response(
            {"error": "username and password required"}, status=status.HTTP_400_BAD_REQUEST
        )

    if User.objects.filter(username=username).exists():
        return Response(
            {"error": "username already exists"}, status=status.HTTP_409_CONFLICT
        )

    user = User.objects.create_user(
        username=username,
        password=password,
        email=email
    )

    return Response({
        "success": True,
        "username": user.username
    })

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user(request):

	user = request.user

	return Response({
		"id": user.id,
		"username": user.username,
		"email": user.email
		})