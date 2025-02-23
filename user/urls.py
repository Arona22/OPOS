from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('edit_profile', views.edit_profile, name='edit_profile'),
    path('profile_details', views.get_user, name='profile_details'),
    path('show_profile', views.show_profile, name='show_profile'),
    
]