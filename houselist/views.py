from django.shortcuts import render
from accounts import views
from houses import views
from houses import models
# Create your views here.


def houseList(request):

    return render(request, 'assigned.html')
