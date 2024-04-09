from rest_framework import serializers
from .models import Release

class ReleaseSerializer(serializers.ModelSerializer):
  class Meta:
    model = Release
    fields = ['id', 'title', 'description', 'tag', 'version', 'created_at', 'author']

  def validate(self, data):
    required_fields = ['title', 'description', 'tag', 'version']
    for field in required_fields:
      if field not in data:
        raise serializers.ValidationError({field: 'Este campo es requerido.'})
    return data