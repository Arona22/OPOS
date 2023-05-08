from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/edit_profile
    path('', views.index, name="edit_profile-index"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('update_user/<int:id>', views.update_user, name="update_user"),

]