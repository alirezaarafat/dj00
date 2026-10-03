from django.db import models
from django.db.models.fields import TextField


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    description = models.TextField(max_length=1000)


    def __str__(self):
      return self.title