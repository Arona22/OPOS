from django.db import models

# Create your models here.
class Pizzas(models.Model):
    name = models.CharField(max_length=2556)