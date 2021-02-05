from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House
from datetime import datetime
from .forms import HouseForm
# Create your views here.


def index(request):
    houses = House.objects.all()
    return render(request, "houses.html", {'houses': houses})


def about(request):
    return render(request, 'about.html')


def insert_view(request):
    form = HouseForm
    if request.method == "POST":
        form = HouseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'insert.html', {'form': form})


def delete_view(request, id):
    houses = House.objects.get(id=id)
    houses.delete()
    return redirect('/')
