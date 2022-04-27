from django.db import models

# Create your models here.
class InventoryItem(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=5000)
    price = models.DecimalField(max_digits=4, decimal_places=2)
