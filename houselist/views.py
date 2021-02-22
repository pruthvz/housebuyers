from django.shortcuts import render
from accounts import views
from houses import views
from houses import models

# Create your views here.


def houseList(request, houseId):
    houses = models.House.objects.get(id=houseId)
    return render(request, 'assigned.html', {'houses': houses})
