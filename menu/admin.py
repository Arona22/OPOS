from django.contrib import admin
from .models import Pizza, Category, Pizza_category, Rating, PizzaImage, Sales

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Category)
admin.site.register(Pizza_category)
admin.site.register(Rating)
admin.site.register(PizzaImage)
admin.site.register(Sales)