from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .models import Home
from .serializers import HomeSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def create_home(request):

    name = request.data.get("name")

    if not name:
        return Response(
            {"error": "Home name required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    home = Home.objects.create(
        name=name,
        owner=None
    )

    serializer = HomeSerializer(home)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([AllowAny])
def list_home(request):

    homes = Home.objects.filter()

    serializer = HomeSerializer(homes, many=True)

    return Response(serializer.data)