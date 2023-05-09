from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True, default='')
    email = models.CharField(max_length=255, unique=True, default='')
    phone = models.CharField(max_length=255, blank=True)
    profile_image = models.CharField(max_length=9999, blank=True)
