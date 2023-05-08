from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/edit_profile
    path('', views.index, name="edit_profile-index"),
    path('create_user', views.create_user, name="create_user"),
    path('delete_user/<int:id>', views.delete_user, name="delete_user"),
    path('update_name/<int:id>', views.update_name, name="update_name"),
    path('update_email/<int:id>', views.update_email, name="update_email"),
    path('update_phone/<int:id>', views.update_phone, name="update_phone"),
]