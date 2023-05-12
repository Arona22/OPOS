from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from menu.models import Pizza


# Create your models here.

class Countries(models.Model):
    name = models.CharField(max_length=255)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField(default=0)
    order_date = models.DateField(default=now())

class Customer_order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)


class Payment(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    cardholder_name = models.CharField(max_length=255, default='')
    card_number = models.IntegerField(default=0)
    card_month = models.IntegerField(default=0)
    card_year = models.IntegerField(default=0)
    card_cvc = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    pament_date = models.DateField(default=now())

class ContactInfo(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.IntegerField(blank=True)