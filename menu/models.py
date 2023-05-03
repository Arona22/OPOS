from django.db import models

# Create your models here.

class Categories(models.Model):
    name = models.CharField(max_length=255)


class Pizzas(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    date_added = models.DateField()
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    

class PizzaImage(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    image = models.CharField(max_length=9999)


class Prices(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    small = models.FloatField()
    medium = models.FloatField()
    large = models.FloatField()


class Sales(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    sales = models.FloatField()


class Ratings(models.Model):
    pizza = models.ForeignKey(Pizzas, on_delete=models.CASCADE)
    rating = models.FloatField()
    
