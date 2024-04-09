from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password', 'date_joined']
    
    def validate(self, data):
        email = data.get('email', None)
        if email is None:
            raise serializers.ValidationError("El campo de correo electrónico es requerido.")
        return data