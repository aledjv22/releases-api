from django.urls import path
from . import views

urlpatterns = [
  path('delete/<int:id>', views.delete_release),
  path('update/<int:id>', views.update_release),
  path('<int:id>', views.get_release),
  path('create', views.create_release),
  path('', views.get_releases),
]