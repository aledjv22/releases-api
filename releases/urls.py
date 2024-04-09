from django.urls import re_path
from . import views

urlpatterns = [
  re_path('', views.get_releases),
  re_path('create', views.create_release),
]