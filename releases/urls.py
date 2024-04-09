from django.urls import re_path, path
from . import views

urlpatterns = [
  path('delete/<int:id>', views.delete_release),
  path('update/<int:id>', views.update_release),
  path('<int:id>', views.get_release),
  re_path('create', views.create_release),
  re_path('', views.get_releases),
]