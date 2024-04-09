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


@api_view(['GET'])
def get_release(request, id):
  try:
    release = Release.objects.get(id=id) 
    serializer = ReleaseSerializer(release)
    return Response({'Release': serializer.data}, status=status.HTTP_200_OK)
  
  except Release.DoesNotExist:
    return Response({'Error': 'El release no existe.'}, status=status.HTTP_404_NOT_FOUND)
  

@api_view(['DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_release(request, id):
  try:
    release = Release.objects.get(id=id)
    
    if release.author != request.user:
      return Response({'Error': 'No tienes permiso para eliminar este release.'}, status=status.HTTP_403_FORBIDDEN)

    release.delete()
    return Response({'Mensaje': 'Release eliminado con exito.'}, status=status.HTTP_200_OK)
  
  except Release.DoesNotExist:
    return Response({'Error': 'El release no existe.'}, status=status.HTTP_404_NOT_FOUND)