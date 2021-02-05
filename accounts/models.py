from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    address = models.CharField(max_length=254)
    date_birth = models.IntegerField()
    buyer_number = models.CharField(max_length=15)
    buyer_solicitor_name = models.CharField(max_length=254)
    household_income = models.IntegerField()

    def __str__(self):
        return self.user.username
