from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Creating the Database variables and data types and creating the table for the database.


class UserProfile(models.Model):
    # the import User is a built in login tool built within django
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # these are the extra additional fields that were added to the database.
    address = models.CharField(max_length=254)
    date_birth = models.IntegerField()
    buyer_number = models.CharField(max_length=15)
    buyer_solicitor_name = models.CharField(max_length=254)
    household_income = models.IntegerField()

    # returns the username from the database, it isn't needed but I kept it here.
    def __str__(self):
        return self.user.username
