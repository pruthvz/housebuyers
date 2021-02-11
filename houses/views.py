# IMPORTS
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import House
from datetime import datetime
from .forms import HouseForm
# Create your views here.
import time

# Dynamic greetings in python.
current_hour = time.strptime(time.ctime(time.time())).tm_hour

# checks with the current time and says the followings.
if current_hour < 12:
    print("Good Morning!")
elif current_hour == 12:
    print("Good Noon!")
elif current_hour > 12 and current_hour < 18:
    print("Good AfterNoon!")
elif current_hour >= 18:
    print("Good Evening!")

# THE INDEX function, takes the entire House modal, from the database and then sends it to the houses.html page


def index(request):
    houses = House.objects.all()  # houses.object.all is a built in function for django
    # the time is the name variable i chose and sent the variable current_hour through to be used in the web page.
    return render(request, "houses.html", {'houses': houses, 'time': current_hour})


# This ABOUT function, will open the about.html page. When the function is called through the navbar.
def about(request):
    return render(request, 'about.html')

# This insert_view function takes in the request of a form. THIS IS A POST REQUEST, which will send the data that is inserted in the html file.


def insert_view(request):
    form = HouseForm  # database fields assigned to the form variable.
    if request.method == "POST":  # checks for the request method
        form = HouseForm(request.POST)  # sends the data.
        if form.is_valid():  # checks if the data that is entered in the html file is valid or not.
            form.save()  # saves the file, these are built in features
            return redirect('/')  # then redirects the user to home.
    # if it isn't valid it will loop until all the fields are entered right.
    return render(request, 'insert.html', {'form': form})


# A simple delete house function. It takes the request and the house ID.
def delete_view(request, id):
    # this is where the variable houses takes the id from the house Database.
    houses = House.objects.get(id=id)
    # a built in function delete deletes the value from the database and from the html file.
    houses.delete()
    return redirect('/')  # redirects to home page again.
