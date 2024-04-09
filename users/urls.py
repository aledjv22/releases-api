from django.urls import path
from . import views

urlpatterns = [
  path('<int:id>/releases', views.user_releases),
  path('login', views.login),
  path('register', views.register),
  path('profile', views.profile),
  path('logout', views.logout),
]