from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255, unique=True)
    phone = models.CharField(max_length=255)
    password = models.CharField()
    proimg = models.CharField(max_length=9999, blank=True)