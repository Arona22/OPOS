from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from menu.models import Pizza


# Create your models here.
class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    order_date = models.DateField(default=now())

