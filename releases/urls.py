from django.urls import re_path,path
from . import views

urlpatterns = [
  path('<int:id>', views.get_release),
  re_path('', views.get_releases),
  re_path('create', views.create_release),
]