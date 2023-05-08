from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/edit_profile
    path('', views.index, name="edit_profile-index"),
    path('create_user', views.create_user, name="create_user"),
]