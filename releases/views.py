from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Release
from .serializers import ReleaseSerializer

@api_view(['POST'])
def create_release(request):
  serializer = ReleaseSerializer(data=request.data)

  if serializer.is_valid():
    serializer.save()

    return Response({'Release': serializer.data}, status=status.HTTP_201_CREATED)
  
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)