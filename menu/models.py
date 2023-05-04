from django.db import models

# Create your models here.

class Categories(models.Model):

    name = models.CharField(max_length=255)


class Pizzas(models.Model):
    name = models.CharField(max_length=255)
    categories = models.ManyToManyField(Categories, related_name='pizzas')
    description = models.CharField(max_length=255, blank=True)
    date_added = models.DateField()
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


class Sales(models.Model):
    pizza = models.OneToOneField (
        Pizzas, 
        primary_key = True,
        on_delete=models.CASCADE        
        )
    sales = models.IntegerField()


class Ratings(models.Model):
    name = models.CharField(max_length=255, primary_key=True, blank=True)
    rating = models.IntegerField()
    
