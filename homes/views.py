from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Home
from .serializers import HomeSerializer

@api_view(['POST'])
def create_home(request):

    user = User.objects.first()

    name = request.data.get("name")

    if not name:
        return Response(
            {"error": "Home name required"},
            status=status.HTTP_400_BAD_REQUEST
        )

    home = Home.objects.create(
        name=name,
        owner=request.user
    )

    serializer = HomeSerializer(home)

    return Response(serializer.data)

@api_view(['GET'])
def list_home(request):

    user = User.objects.first()

    homes = Home.objects.filter(owner=request.user)

    serializer = HomeSerializer(homes, many=True)

    return Response(serializer.data)