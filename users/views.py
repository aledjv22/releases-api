from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from .serializers import UserSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def login (request):
    email = request.data.get('email')
    password = request.data.get('password')

    if not email and not password:
        return Response({"Error": "Se requieren los campos de email y password."}, status=status.HTTP_400_BAD_REQUEST)
    
    elif not email:
        return Response({"Error": "Se requiere el campo de email."}, status=status.HTTP_400_BAD_REQUEST)
    
    elif not password:
        return Response({"Error": "Se requiere el campo de password."}, status=status.HTTP_400_BAD_REQUEST)
    
    else: 
        user = get_object_or_404(User, email=email)

    if not user.check_password(request.data['password']):
        return Response({"Error": "Contraseña incorrecta."}, status=status.HTTP_400_BAD_REQUEST)
    
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)

    return Response({
        'token': token.key,
        'user': serializer.data
    }, status=status.HTTP_200_OK)


@api_view(['POST'])
def register (request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()

        token = Token.objects.create(user=user)
        return Response({
            'token': token.key, 
            "user": serializer.data 
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
