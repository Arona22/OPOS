from django.contrib import admin
from .models import Order, Customer_order


# Register your models here.
admin.site.register(Order)
admin.site.register(Customer_order)

