from django.contrib import admin
from .models import Order, Customer_order, Payment, ContactInfo, Countries


# Register your models here.
admin.site.register(Order)
admin.site.register(Customer_order)
admin.site.register(Payment)
admin.site.register(ContactInfo)
admin.site.register(Countries)

