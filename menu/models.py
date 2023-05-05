from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Ratings(models.Model):
    name = models.CharField(max_length=255)
    rating = models.IntegerField()

# from menu.models import Pizzas, Categories, Pizza_category, Ratings, PizzaImage, Sales

class Pizzas(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Categories, related_name='pizzas')
    ratings = models.ManyToManyField(Ratings, related_name='pizzas')
    description = models.CharField(max_length=255, blank=True)
    created_at = models.DateField()
    is_new = models.BooleanField(default=False)
    price_small = models.IntegerField(default=1199)
    price_medium = models.IntegerField(default=2199)
    price_large = models.IntegerField(default=3199)

    def __str__(self) -> str:
        return self.name


class Pizza_category(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete = models.CASCADE)
    category = models.ForeignKey(Categories, on_delete = models.CASCADE)


class PizzaImage(models.Model):
    pizza = models.ForeignKey (
        Pizzas, 
        on_delete = models.CASCADE, 
        default = ''
        )
    image = models.CharField(max_length=9999, blank=True)

    def __str__(self) -> str:
        return self.image


class Sales(models.Model):
    pizza = models.OneToOneField (
        Pizzas, 
        primary_key = True,
        on_delete=models.CASCADE        
        )
    sales = models.IntegerField()



    
