from django.contrib import admin
from .models import Pizzas, Categories, Pizza_category, Ratings, PizzaImage, Sales

# Register your models here.
admin.site.register(Pizzas)
admin.site.register(Categories)
admin.site.register(Pizza_category)
admin.site.register(Ratings)
admin.site.register(PizzaImage)
admin.site.register(Sales)