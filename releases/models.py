from django.db import models
from django.contrib.auth.models import User

class Release(models.Model):
  id = models.AutoField(primary_key=True)
  title = models.CharField(max_length=200)
  description = models.TextField()
  tag = models.CharField(max_length=200)
  version = models.CharField(max_length=200)
  created_at = models.DateField(auto_now_add=True)
  author = models.ForeignKey(User, on_delete=models.CASCADE)
