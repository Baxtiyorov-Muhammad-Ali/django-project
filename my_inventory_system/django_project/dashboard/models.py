from django.db import models
from django.core.validators import MinValueValidator
class Product(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(validators=[MinValueValidator(0)])

