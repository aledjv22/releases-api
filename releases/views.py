from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ReleaseSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .models import Release


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def create_release(request):
  data = request.data.copy()  # Realizo una copia de los datos
  data['author'] = request.user.id  # Asigno el id del usuario logueado al campo 'author'
  serializer = ReleaseSerializer(data=data) 

  if serializer.is_valid():
    serializer.save()

    return Response({'Release': serializer.data}, status=status.HTTP_201_CREATED)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_releases(request):
  serializer = ReleaseSerializer(instance=Release.objects.all(), many=True)

  return Response({'Releases': serializer.data}, status=status.HTTP_200_OK)
