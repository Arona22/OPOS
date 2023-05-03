from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)


class Pizzas(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    date_added = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    price_small = models.IntegerField(default = 1999)
    price_medium = models.IntegerField(default = 2999)
    price_large = models.IntegerField(default = 3999)

    def __str__(self) -> str:
        return self.name
    

class PizzaImage(models.Model):
    pizza = models.ForeignKey(
        Pizzas, 
        on_delete = models.CASCADE, 
        default = ''
        )
    image = models.CharField(max_length=9999, blank=True)


class Sales(models.Model):
    pizza = models.OneToOneField(
        Pizzas, 
        on_delete=models.CASCADE, 
        primary_key = True,
        )
    sales = models.FloatField()


class Ratings(models.Model):
    pizza = models.OneToOneField(
        Pizzas, 
        on_delete=models.CASCADE, 
        primary_key = True,
        )
    rating = models.FloatField()
    
