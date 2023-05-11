from django.db import models

# Create your models here.
class Offers(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    image = models.CharField(max_length=9999, blank=True)

class OfferImage(models.Model):
    offer = models.ForeignKey(
        Offers, 
        on_delete=models.CASCADE, 
        default=''
        )
    image = models.CharField(max_length=9999, blank=True)
    
