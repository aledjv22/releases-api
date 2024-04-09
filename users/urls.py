from django.urls import re_path, path
from . import views

urlpatterns = [
  path('<int:id>/releases', views.user_releases),
  re_path('login', views.login),
  re_path('register', views.register),
  re_path('profile', views.profile),
  re_path('logout', views.logout),
]