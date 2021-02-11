from django.db import models

# Create your models here.

# This PostgreSQL Modal, which contains all the fields.
# All these variables will be stored within my PostgreSQL with the name variables and the field type.


class House(models.Model):
    owner = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    types = models.CharField(max_length=255)
    bedroomNo = models.IntegerField()
    price = models.IntegerField()
    sellerName = models.CharField(max_length=255)
    sellNo = models.BigIntegerField()
    solicitorName = models.CharField(max_length=255)
    desc = models.TextField()
    offer = models.BooleanField(default=False)
